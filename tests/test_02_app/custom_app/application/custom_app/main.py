import sys

from flask import Flask

custom_app = Flask(__name__)


@custom_app.route("/api")
def hello():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    message = "Hello World from Flask in a uWSGI Nginx Docker container with Python {} - testing".format(
        version
    )
    return message


@custom_app.route("/")
def main():
    return "API response overriden by Nginx"


@custom_app.route("/content/test.txt")
def static_test():
    return "Not run, Nginx overrides to serve static file"


if __name__ == "__main__":
    custom_app.run(host="0.0.0.0", debug=True, port=80)
