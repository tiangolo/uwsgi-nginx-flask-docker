from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 2.7 (default)"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
