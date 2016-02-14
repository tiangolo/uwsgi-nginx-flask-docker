# uwsgi-nginx-flask

**Docker** image with **uWSGI** and **Nginx** for **Flask** applications in **Python** running in a single container.

## Description

This Docker image allows you to create [**Flask**](http://flask.pocoo.org/) applications in [**Python**](https://www.python.org/) that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/).

uWSGI with Nginx is one of the best ways to deploy a Python application, so you you should have a [good performance (check the benchmarks)](http://nichol.as/benchmark-of-python-web-servers) with this image.

**GitHub repo**: <https://github.com/tiangolo/uwsgi-nginx-flask-docker>
**Docker Hub image**: <https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/>

## General Instructions

You don't have to clone this repo, you should be able to use this image as a base image for your project.

There are two image tags:

* **`flask`** (also `latest`): An image based on the [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) image. This image includes Flask and a sample template app.

The image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) has uWSGI and Nginx installed in the same container and is made to be the base of this image.

You probably want to use this (`uwsgi-nginx-flask:flask`) as your base image.

* **`flask-index`**: An image based on the **`flask`** image, but optimizing the configuration to make Nginx serve `/app/static/index.html` directly when requested for `/`.
This is specially helpful (and efficient) if you are building a single-page app without templates (as with Angular JS) and using Flask as an API / back-end.

## Creating a Flask Docker project

You may use the files in this example and use them as the template for your project:

---

Or you may follow the instructions to build it from scratch:

* Go to your project directory
* Create a `Dockerfile` with:

```
FROM tiangolo/uwsgi-nginx-flask:flask

COPY ./app /app
```

* Create an `app` directory and enter in it
* Create a `main.py` file (it should be named like that and should be in your `app` directory) with:

 ```
 from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
 ```

 the main application object should be named `app` (in the code) as in this example.

* Go to the project directory (in where your `Dockerfile` is, containing your `app` directory)
* Build your Flask image:

```
docker build -t myimage .
```

* Run a container based on your image:

```
docker run -d --name mycontainer -p 80:80 myimage
```

...and you have an optimized Flask server in a Docker container.

## Creating an Angular JS app (or similar) with Flask with Docker

You may use the files in this example and use them as the template for your project:

---

Or you may follow the instructions to build it from scratch (it's very similar to the instructions above):

* Go to your project directory
* Create a `Dockerfile` with:

```
FROM tiangolo/uwsgi-nginx-flask:flask-index

COPY ./app /app
```

* Create an `app` directory and enter in it
* Create a `main.py` file (it should be named like that and should be in your `app` directory) with:

```
from flask import Flask, send_file
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World from Flask"

@app.route("/")
def main():
    return send_file('./static/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
```

 the main application object should be named `app` (in the code) as in this example.

* Make sure you have an `index.html` file in `./app/static/index.html`, for example with:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
<h1>Hello World from HTML</h1>
</body>
</html>
```

* Go to the project directory (in where your `Dockerfile` is, containing your `app` directory)
* Build your Flask image:

```
docker build -t myimage .
```

* Run a container based on your image:

```
docker run -d --name mycontainer -p 80:80 myimage
```

...and you have an optimized Flask server in a Docker container. Also optimized to serve your main non-templated `index.html` page.

* Now, when you go to your Docker container URL, for example: <http://192.168.99.100/>, you will see your `index.html` as if you were in <http://192.168.99.100/static/index.html>.


## Technical details

One of the best ways to deploy a Python application is with uWSGI and Nginx, as seen in the [benchmarks](http://nichol.as/benchmark-of-python-web-servers).

Roughly:

* **Nginx** is a web server, it takes care of the HTTP connections and also can serve static files directly and more efficiently.

* **uWSGI** is an application server, that's what runs your Python code.

* **Your Python code** has the actual application, and is run by uWSGI.

The image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) takes advantage of already slim and optimized existing Docker images (based on Debian as [recommended by Docker](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)) and implements Docker best practices.

It uses the official Python Docker image, installs uWSGI and on top of that, with the least amount of modifications, adds the official Nginx image (as of 2016-02-14).

This image is based on the image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) and adds Flask and sensible defaults on top of it.

If you follow the instructions and keep the root directory `/app` in your container, with a file named `main.py` and a Flask object named `app` in it, it should "just work".

There's already a `uwsgi.ini` file in the `/app` directory with the uWSGI configurations for it to "just work".

If you need to change the main file name or the main Flask object, you would have to provide your own `uwsgi.ini` file. You may use the file in this repo as a template to start with (you only would have to change 2 lines).

You can have a `/app/static` directory and those files will be efficiently served by Nginx directly, it's already configured for you.

Supervisord takes care of running uWSGI with that `uwsgi.ini` file and start Nginx.

---

There's the rule of thumb that you should have "one process per container".

That helps, for example, isolating an app from its database in different containers.

But if you want to have a "micro-services" approach you may want to [have more than one process in one container](https://valdhaus.co/writings/docker-misconceptions/) if they are all related to the same "service", and you may want to include your Flask code, uWSGI and Nginx in the same container (and maybe run another container with your database).

That's the approach taken in this image.

## Advanced instructions



## License

This project is licensed under the terms of the Apache license.