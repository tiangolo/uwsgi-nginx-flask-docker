from ..main import app
from ..api import api


@app.route("/")
def hello():
    # This could also be returning an index.html
    return '''Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.6 (from the example template), 
     try also: <a href="/users/">/users/</a>'''
