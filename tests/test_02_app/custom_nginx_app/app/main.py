import sys

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    message = "Hello World from Flask in a uWSGI Nginx Docker container with Python {} - testing".format(
        version
    )
    return message


@app.route("/static/test.txt")
def static_test():
    return "Static, from Flask"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
