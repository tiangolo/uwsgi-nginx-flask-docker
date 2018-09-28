from flask import Flask
# StatsD: https://statsd.readthedocs.io/en/v3.2.1/timing.html
from statsd import StatsClient
import time
import random
app = Flask(__name__)
statsd = StatsClient(host='localhost',
                     port=8126,
                     prefix='services',
                     maxudpsize=512)


@app.route("/")
@statsd.timer("test_service.response_time")
def hello():
    time.sleep(round(random.uniform(0.1, 1), 3))
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
         Python 3.6 (default)"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8888)
