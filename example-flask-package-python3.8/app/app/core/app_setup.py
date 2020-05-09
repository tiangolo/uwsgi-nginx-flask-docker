from ..api import api  # noqa
from ..main import app


@app.route("/")
def hello():
    # This could also be returning an index.html
    return """Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (from the example template), 
     try also: <a href="/users/">/users/</a>"""
