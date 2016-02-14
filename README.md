# uwsgi-nginx-flask

**Docker** image with **uWSGI** and **Nginx** for **Python Flask** applications in a single container.

## Description

This Docker image allows you to create [**Flask**](http://flask.pocoo.org/) applications in [**Python**](https://www.python.org/) that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/).

uWSGI with Nginx is one of the best ways to deploy a Python application, so you you should have a good performance with this image.

## General Instructions

You don't have to clone this repo, you should be able to use this image as a base image for your project.

There are two image tags:

* **`flask`** (also `latest`): An image based on the **tiangolo/uwsgi-nginx** image, including Flask and a sample template app.

The image **tiangolo/uwsgi-nginx** has uWSGI and Nginx installed in the same container and is made to be the base of this image.

You probably want to use this as your base image.

* **`flask-index`**: An image based on the **flask** image, but optimizing the configuration to make Nginx serve `/app/static/index.html` directly when requested for `/`.
This is specially helpful (and efficient) if you are building a single-page app without templates (as with Angular JS) and using Flask as an API / back-end.

## Creating a Flask Docker project

You may use the files in this example and use them as the template for your project:

* Go to your project directory
* Create a `Dockerfile` with:

```
FROM tiangolo/uwsgi-nginx-flask:flask

COPY ./app /app
```

* Create an `app` directory:

```
mkdir app
```

* Enter the `app` directory:

 ```
 cd app
 ```

* Create a `main.py` file (it should be named like that) with:

 ```
 from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print "test"
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)

 ```

 (the main application should be named `app` as in this example).

* Get to the project directory (in where your `Dockerfile` is):

```
cd ..
```

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

* Do the same as above but create the `Dockerfile` with:

```
FROM tiangolo/uwsgi-nginx-flask:flask-index

COPY ./app /app
```

* Make sure you have an `index.html` file in `./app/static/index.html`, for example with:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
<h1>Hello World</h1>
</body>
</html>
```

* Now, when you go to your Docker container URL, for example: <http://192.168.99.100/>, you will see your `index.html` as if you were in <http://192.168.99.100/static/index.html>.


## Technical details

One of the best ways to deploy a Python application is with uWSGI and Nginx, as seen in the [benchmarks](http://nichol.as/benchmark-of-python-web-servers).

Roughly:

* **Nginx** is a web server, it takes care of the HTTP connections and also can serve static files directly and more efficiently.

* **uWSGI** is an application server, that's what runs your Python code.

* **Your Python code** has the actual application, and is run by uWSGI.

This image (and its tags) take advantage of already slim and optimized existing Docker images (based on Debian as [recommended by Docker](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)), implementing Docker best practices.
It uses the official Python Docker image, installs uWSGI and on top of that, with the least amount of modifications, adds the official Nginx image (as of 2016-02-14).

There's the rule of thumb that you should have "one process per container".
That helps, for example, isolating an app from its database in different containers.
But if you want to have a "micro-services" approach you may want to [have more than one process in one container](https://valdhaus.co/writings/docker-misconceptions/) if they are all related to the same "service", and you may want to include your code, uWSGI and Nginx in the same container (and maybe run another container with your database).

That's the approach taken in this image.

## License

This project is licensed under the terms of the Apache license.