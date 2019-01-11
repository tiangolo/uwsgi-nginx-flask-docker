import time
from pathlib import Path, PurePath

import docker
import pytest
import requests

from ..utils import CONTAINER_NAME, get_logs, get_nginx_config, stop_previous_container

client = docker.from_env()


@pytest.mark.parametrize(
    "dockerfile,response_text",
    [
        (
            "python2.7.dockerfile",
            "Hello World from Flask in a uWSGI Nginx Docker container with Python 2.7 - testing",
        ),
        (
            "python2.7-alpine3.7.dockerfile",
            "Hello World from Flask in a uWSGI Nginx Docker container with Python 2.7 - testing",
        ),
        (
            "python2.7-alpine3.8.dockerfile",
            "Hello World from Flask in a uWSGI Nginx Docker container with Python 2.7 - testing",
        ),
        (
            "python3.5.dockerfile",
            "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.5 - testing",
        ),
        (
            "python3.6.dockerfile",
            "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.6 - testing",
        ),
        (
            "python3.6-alpine3.7.dockerfile",
            "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.6 - testing",
        ),
        (
            "python3.6-alpine3.8.dockerfile",
            "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.6 - testing",
        ),
        (
            "python3.7.dockerfile",
            "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 - testing",
        ),
        (
            "latest.dockerfile",
            "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 - testing",
        ),
        # (
        #     "python3.7-alpine3.7.dockerfile",
        #     "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 - testing",
        # ),
        # (
        #     "python3.7-alpine3.8.dockerfile",
        #     "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 - testing",
        # ),
    ],
)
def test_env_vars_1(dockerfile, response_text):
    stop_previous_container(client)
    tag = "uwsgi-nginx-flask-testimage"
    test_path: PurePath = Path(__file__)
    path = test_path.parent / "simple_app"
    client.images.build(path=str(path), dockerfile=dockerfile, tag=tag)
    container = client.containers.run(
        tag, name=CONTAINER_NAME, ports={"80": "8000"}, detach=True
    )
    nginx_config = get_nginx_config(container)
    assert "client_max_body_size 0;" in nginx_config
    assert "worker_processes 1;" in nginx_config
    assert "listen 80;" in nginx_config
    assert "worker_connections  1024;" in nginx_config
    assert "worker_rlimit_nofile;" not in nginx_config
    assert "daemon off;" in nginx_config
    assert "include uwsgi_params;" in nginx_config
    assert "uwsgi_pass unix:///tmp/uwsgi.sock;" in nginx_config
    assert "try_files $uri @app;" in nginx_config
    assert "location @app {" in nginx_config
    assert "include uwsgi_params;" in nginx_config
    assert "location /static {" in nginx_config
    assert "alias /app/static;" in nginx_config
    # Nginx index.html specific
    assert "location = / {" not in nginx_config
    assert "index /static/index.html;" not in nginx_config
    time.sleep(5)
    logs = get_logs(container)
    assert "getting INI configuration from /app/uwsgi.ini" in logs
    assert "getting INI configuration from /etc/uwsgi/uwsgi.ini" in logs
    assert "ini = /app/uwsgi.ini" in logs
    assert "ini = /etc/uwsgi/uwsgi.ini" in logs
    assert "socket = /tmp/uwsgi.sock" in logs
    assert "chown-socket = nginx:nginx" in logs
    assert "chmod-socket = 664" in logs
    assert "hook-master-start = unix_signal:15 gracefully_kill_them_all" in logs
    assert "need-app = true" in logs
    assert "die-on-term = true" in logs
    assert "show-config = true" in logs
    assert "module = main" in logs
    assert "callable = app" in logs
    assert "processes = 16" in logs
    assert "cheaper = 2" in logs
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )
    assert "spawned uWSGI master process" in logs
    assert "spawned uWSGI worker 1" in logs
    assert "spawned uWSGI worker 2" in logs
    assert "spawned uWSGI worker 3" not in logs
    assert 'running "unix_signal:15 gracefully_kill_them_all" (master-start)' in logs
    assert "success: nginx entered RUNNING state, process has stayed up for" in logs
    assert "success: uwsgi entered RUNNING state, process has stayed up for" in logs
    response: Response = requests.get("http://127.0.0.1:8000")
    assert response.status_code == 200
    assert response.text == response_text
    response: Response = requests.get("http://127.0.0.1:8000/static/test.txt")
    assert response.status_code == 200
    assert response.text == "Static test"
    container.stop()
    container.remove()
