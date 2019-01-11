import sys

from flask import Flask, send_file

app = Flask(__name__)


@app.route("/api")
def hello():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    message = "Hello World from Flask in a uWSGI Nginx Docker container with Python {} (default)".format(
        version
    )
    return message


@app.route("/")
def main():
    return send_file("./static/index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
