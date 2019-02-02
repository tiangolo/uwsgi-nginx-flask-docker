from docker.errors import NotFound

CONTAINER_NAME = "uwsgi-nginx-flask-test"


def get_logs(container):
    logs: str = container.logs()
    return logs.decode("utf-8")


def get_nginx_config(container):
    result = container.exec_run(f"/usr/sbin/nginx -T")
    return result.output.decode()


def remove_previous_container(client):
    try:
        previous = client.containers.get(CONTAINER_NAME)
        previous.stop()
        previous.remove()
    except NotFound:
        return None
