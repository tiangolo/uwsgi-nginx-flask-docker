import os

from docker.client import DockerClient
from docker.errors import NotFound
from docker.models.containers import Container

CONTAINER_NAME = "uwsgi-nginx-flask-test"


def get_logs(container: Container) -> str:
    logs = container.logs()
    return logs.decode("utf-8")


def get_nginx_config(container: Container) -> str:
    result = container.exec_run(f"/usr/sbin/nginx -T")
    return result.output.decode()


def remove_previous_container(client: DockerClient) -> None:
    try:
        previous = client.containers.get(CONTAINER_NAME)
        previous.stop()
        previous.remove()
    except NotFound:
        return None


def get_response_text1() -> str:
    python_version = os.getenv("PYTHON_VERSION")
    return f"Hello World from Flask in a uWSGI Nginx Docker container with Python {python_version} (default)"


def get_response_text2() -> str:
    python_version = os.getenv("PYTHON_VERSION")
    return f"Hello World from Flask in a uWSGI Nginx Docker container with Python {python_version} - testing"


def generate_dockerfile_content_custom_app(name: str) -> str:
    content = f"FROM tiangolo/uwsgi-nginx-flask:{name}\n"
    content += "COPY ./application /application\n"
    content += "COPY ./prestart.sh /app/prestart.sh\n"
    content += "WORKDIR /application\n"
    return content


def generate_dockerfile_content_custom_nginx_app(name: str) -> str:
    content = f"FROM tiangolo/uwsgi-nginx-flask:{name}\n"
    content += "COPY app /app\n"
    return content


def generate_dockerfile_content_simple_app(name: str) -> str:
    content = f"FROM tiangolo/uwsgi-nginx-flask:{name}\n"
    content += "COPY ./app/ /app/\n"
    return content
