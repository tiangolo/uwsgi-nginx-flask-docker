# uwsgi-nginx-flask

**Docker** image with **uWSGI** and **Nginx** for **Flask** applications in **Python** running in a single container.

## Description

This Docker image allows you to create [**Flask**](http://flask.pocoo.org/) applications in [**Python**](https://www.python.org/) that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/) in a single container.

uWSGI with Nginx is one of the best ways to deploy a Python application, so you you should have a [good performance (check the benchmarks)](http://nichol.as/benchmark-of-python-web-servers) with this image.

**GitHub repo**: <https://github.com/tiangolo/uwsgi-nginx-flask-docker>

**Docker Hub image**: <https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/>

## General Instructions

You don't have to clone this repo, you should be able to use this image as a base image for your project.

There are two image tags:

* **`flask`** (also `latest`): An image based on the [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) image. This image includes Flask and a sample template app.

The image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) has uWSGI and Nginx installed in the same container and is made to be the base of this image.

Use `FROM tiangolo/uwsgi-nginx-flask:flask` in your `Dockerfile` to use this image. (This would be the most general "default" image).

* **`flask-index`**: An image based on the **`flask`** image (above), but optimizing the configuration to make Nginx serve `/app/static/index.html` directly (instead of going through uWSGI and your code) when requested for `/`.

This is specially helpful (and efficient) if you are building a single-page app without templates (as with Angular JS) and using Flask as an API / back-end.

Use `FROM tiangolo/uwsgi-nginx-flask:flask-index` in your `Dockerfile` to use this image.

## Creating a Flask project with Docker

**Note**: These instructions are for the `flask` tag and are intended for a general purpose Flask application.

You can download these example files and use them as the template for your project:

---

Or you may follow the instructions to build your project from scratch:

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

You should be able to check it in your Docker container's URL, for example: <http://192.168.99.100/>

## Creating an Angular JS (or similar) and Flask project with Docker

**Note**: These instructions are for the `flask-index` tag and are intended for an application that serves a static `index.html` file, as in an Angular JS application.

You can download these example files and use them as the template for your project:

---

Or you may follow the instructions to build your project from scratch (it's very similar to the procedure above):

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

**Note**: The section with the `main()` function is for debugging purposes. To learn more, read the **Advanced instructions** below.

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

* You should be able to also go to, for example: <http://192.168.99.100/hello> to see a "Hello World" page served by Flask.


## Technical details

One of the best ways to deploy a Python application is with uWSGI and Nginx, as seen in the [benchmarks](http://nichol.as/benchmark-of-python-web-servers).

Roughly:

* **Nginx** is a web server, it takes care of the HTTP connections and also can serve static files directly and more efficiently.

* **uWSGI** is an application server, that's what runs your Python code.

* **Your Python code** has the actual **Flask** application, and is run by uWSGI.

The image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) takes advantage of already slim and optimized existing Docker images (based on Debian as [recommended by Docker](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)) and implements Docker best practices.

It uses the official Python Docker image, installs uWSGI and on top of that, with the least amount of modifications, adds the official Nginx image (as of 2016-02-14).

The image (and tags) created by this repo is based on the image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) and adds Flask and sensible defaults on top of it.

If you follow the instructions and keep the root directory `/app` in your container, with a file named `main.py` and a Flask object named `app` in it, it should "just work".

There's already a `uwsgi.ini` file in the `/app` directory with the uWSGI configurations for it to "just work".

If you need to change the main file name or the main Flask object, you would have to provide your own `uwsgi.ini` file. You may use the one in this repo as a template to start with (you only would have to change 2 lines).

You can have a `/app/static` directory and those files will be efficiently served by Nginx directly (without going through your Flask code or even uWSGI), it's already configured for you.

Supervisord takes care of running uWSGI with the `uwsgi.ini` file in `/app` file and starting Nginx.

---

There's the rule of thumb that you should have "one process per container".

That helps, for example, isolating an app from its database in different containers.

But if you want to have a "micro-services" approach you may want to [have more than one process in one container](https://valdhaus.co/writings/docker-misconceptions/) if they are all related to the same "service", and you may want to include your Flask code, uWSGI and Nginx in the same container (and maybe run another container with your database).

That's the approach taken in this image.

---

You should be aware that these images have some default files, so if you run them by themselves (not as the base images of your own project) you will see a default "Hello World" web app.

When you build a `Dockerfile` with a `COPY ./app /app` you replace those default files with your app code.

The main default file is only in `/app/main.py`. And in the case of the tag `flask-index`, also in `/app/static/index.html`.

But those files render a "(default)" text in the served web page, so that you can check if you are seeing the default code or your own code overriding the default.

The default is that your app code should be in the container's `/app` directory, it should have a `main.py` file (or somehow a `main` module) and that `main.py` file (or module) should have a Flask object `app`.

If you follow the instructions above or use one of the downloadable example templates, you should be OK with those defaults.

There is also a `/app/uwsgi.ini` file inside the images with the default parameters for uWSGI.

In the downloadable examples is a copy of the same `uwsgi.ini` file for debugging purposes. To learn more, read the **Advanced instructions** below.

## Advanced instructions

While developing, you might want to make your code directory a volume in your Docker container.

With that you would have your files (temporarily) updated every time you modify them, without needing to build your container again.

To do this, you can use the command `pwd` (print working directory) inside your `docker run` and the flag `-v` for volumes.

With that you could map your `./app` directory to your container's `/app` directory.

But first, as you will be completely replacing the directory `/app` in your container (and all of its contents) you will need to have a `uwsgi.ini` file in your `./app` directory with:

```
[uwsgi]
socket = /tmp/uwsgi.sock
chown-socket = nginx:nginx
chmod-socket = 664

module = main
callable = app
```

and then you can do the Docker volume mapping.

**Note**: A `uwsgi.ini` file is included in the downloadable examples.

* To try it go to your project directory (the one with your `Dockerfile` and your `./app` directory)
* Make sure you have a `uwsgi.ini` file in your `./app` directory
* Build your Docker image:

```
docker build -t myimage .
```

* Run a container based on your image, mapping your code directory (`./app`) to your container's `/app` directory:

```
docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app myimage
```

if you go to your Docker container URL you should see your app, and you should be able to modify, files in `./app/static/` and see those changes reflected in your browser just by reloading.

...but, as uWSGI loads your whole Python Flask application once it starts, you won't be able to edit your Python code and see the changes reflected.

To be able to (temporarily) debug your Flask code live, you can run your container overriding the default command (that starts Supervisord which in turn starts uWSGI and Nginx) and run your application directly with Python, in debug mode.

So, with all the modifications above and making your app run directly with Python, the final Docker command would be:

 ```
docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app myimage python /app/main.py
```

Now you can edit your Flask code in your local machine and once you refresh your browser you will see the changes live.

Remember that you should use this only for debugging and development, for deployment you shouldn't mount volumes and you should let Supervisord start and let it start uWSGI and Nginx (which is what happens by default).

For these last steps to work (live debugging and development), your Python code should have that section with:

 ```
 if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
 ```

otherwise your app will only listen to localhost (inside the container), in another port (5000) and not in debug mode.

---

Also, if you want to do the same live debugging using the `flask-index` tag (to serve `/app/static/index.html` directly when requested for `/`) your Nginx won't serve it directly as it won't be running (only your Flask app in debug mode will be running).

For that, your Python code should have that section with:

```
from flask import Flask, send_file
```

and

```
@app.route("/")
def main():
    return send_file('./static/index.html')
```

that makes sure your app also serves the `/app/static/index.html` file when requested for `/`.

 That's how it is written in the tutorial above and is included in the downloadable examples.

## License

This project is licensed under the terms of the Apache license.