from flask import Flask, send_file
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.5 (default)"

@app.route("/")
def main():
    return send_file('./static/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
