import os
import time
from pathlib import Path, PurePath

import docker
import pytest
import requests

from ..utils import (
    CONTAINER_NAME,
    get_logs,
    get_nginx_config,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container, response_text):
    nginx_config = get_nginx_config(container)
    assert "client_max_body_size 0;" in nginx_config
    assert "worker_processes 1;" in nginx_config
    assert "listen 8080;" in nginx_config
    assert "worker_connections 1024;" in nginx_config
    assert "worker_rlimit_nofile;" not in nginx_config
    assert "daemon off;" in nginx_config
    assert "include uwsgi_params;" in nginx_config
    assert "uwsgi_pass unix:///tmp/uwsgi.sock;" in nginx_config
    # Nginx index.html specific
    assert "location /content {" in nginx_config
    assert "index /content/index.html;" in nginx_config
    assert "location = / {" in nginx_config
    assert "alias /application/custom_app/content;" in nginx_config
    logs = get_logs(container)
    assert "getting INI configuration from /application/custom_app/uwsgi.ini" in logs
    assert "getting INI configuration from /etc/uwsgi/uwsgi.ini" in logs
    assert "ini = /application/custom_app/uwsgi.ini" in logs
    assert "ini = /etc/uwsgi/uwsgi.ini" in logs
    assert "socket = /tmp/uwsgi.sock" in logs
    assert "chown-socket = nginx:nginx" in logs
    assert "chmod-socket = 664" in logs
    assert "hook-master-start = unix_signal:15 gracefully_kill_them_all" in logs
    assert "need-app = true" in logs
    assert "die-on-term = true" in logs
    assert "show-config = true" in logs
    assert "module = custom_app.main" in logs
    assert "callable = custom_app" in logs
    assert "processes = 16" in logs
    assert "cheaper = 2" in logs
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert "custom prestart.sh running" in logs
    assert "spawned uWSGI master process" in logs
    assert "spawned uWSGI worker 1" in logs
    assert "spawned uWSGI worker 2" in logs
    assert "spawned uWSGI worker 3" not in logs
    assert 'running "unix_signal:15 gracefully_kill_them_all" (master-start)' in logs
    assert "success: nginx entered RUNNING state, process has stayed up for" in logs
    assert "success: uwsgi entered RUNNING state, process has stayed up for" in logs
    response = requests.get("http://127.0.0.1:8000")
    assert response.status_code == 200
    assert (
        response.text == "<html><body><h1>Hello World from HTML test</h1></body></html>"
    )
    response = requests.get("http://127.0.0.1:8000/api")
    assert response.status_code == 200
    assert response.text == response_text
    response = requests.get("http://127.0.0.1:8000/content/test.txt")
    assert response.status_code == 200
    assert response.text == "Static test"


def test_env_vars_1():
    if not os.getenv("RUN_TESTS"):
        return
    name = os.getenv("NAME")
    # It's an index postfix tag, skip it
    if "index" in name:
        return
    dockerfile = f"{name}.dockerfile"
    response_text = os.getenv("TEST_STR2")
    sleep_time = int(os.getenv("SLEEP_TIME", 3))
    remove_previous_container(client)
    tag = "uwsgi-nginx-flask-testimage"
    test_path: PurePath = Path(__file__)
    path = test_path.parent / "custom_app"
    client.images.build(path=str(path), dockerfile=dockerfile, tag=tag)
    container = client.containers.run(
        tag,
        name=CONTAINER_NAME,
        environment={
            "UWSGI_INI": "/application/custom_app/uwsgi.ini",
            "LISTEN_PORT": "8080",
            "STATIC_URL": "/content",
            "STATIC_PATH": "/application/custom_app/content",
            "STATIC_INDEX": 1,
        },
        ports={"8080": "8000"},
        detach=True,
    )
    time.sleep(sleep_time)
    verify_container(container, response_text)
    container.stop()
    # Test that everything works after restarting too
    container.start()
    time.sleep(sleep_time)
    verify_container(container, response_text)
    container.stop()
    container.remove()
