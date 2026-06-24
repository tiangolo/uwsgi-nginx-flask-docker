## DEPRECATED 🚨

This Docker image is now deprecated. Read about it below.

---

[![Test](https://github.com/tiangolo/uwsgi-nginx-flask-docker/actions/workflows/test.yml/badge.svg)](https://github.com/tiangolo/uwsgi-nginx-flask-docker/actions/workflows/test.yml) [![Deploy](https://github.com/tiangolo/uwsgi-nginx-flask-docker/workflows/Deploy/badge.svg)](https://github.com/tiangolo/uwsgi-nginx-flask-docker/actions?query=workflow%3ADeploy)

## Supported tags and respective `Dockerfile` links

* [`python3.12`, `latest` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/docker-images/python3.12.dockerfile)
* [`python3.11`, _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/docker-images/python3.11.dockerfile)
* [`python3.10` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/docker-images/python3.10.dockerfile)

## Deprecated tags

🚨 These tags are no longer supported or maintained, they are removed from the GitHub repository, but the last versions pushed might still be available in Docker Hub if anyone has been pulling them:

* `python3.9`
* `python3.8`
* `python3.8-alpine`
* `python3.7`
* `python3.6`
* `python2.7`

The last date tags for these versions are:

* * `python3.9-2025-11-09`
* `python3.8-2024-10-28`
* `python3.8-alpine-2024-03-11`
* `python3.7-2024-10-28`
* `python3.6-2022-11-25`
* `python2.7-2022-11-25`

---

**Note**: There are [tags for each build date](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/tags). If you need to "pin" the Docker image version you use, you can select one of those tags. E.g. `tiangolo/uwsgi-nginx-flask:python3.7-2019-10-14`.

# uwsgi-nginx-flask

**Docker** image with **uWSGI** and **Nginx** for **Flask** web applications in **Python** running in a single container.

## Description

This [**Docker**](https://www.docker.com/) image allows you to create [**Flask**](http://flask.pocoo.org/) web applications in [**Python**](https://www.python.org/) that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/) in a single container.

The combination of uWSGI with Nginx is a [common way to deploy Python Flask web applications](http://flask.pocoo.org/docs/1.0/deploying/uwsgi/).

---

**GitHub repo**: [https://github.com/tiangolo/uwsgi-nginx-flask-docker](https://github.com/tiangolo/uwsgi-nginx-flask-docker)

**Docker Hub image**: [https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)

## 🚨 DEPRECATION WARNING

You are probably using **Kubernetes** or similar tools. In that case, you probably **don't need this image** (or any other **similar base image**). You are probably better off **building a Docker image from scratch**.

---

If you have a cluster of machines with **Kubernetes**, Docker Swarm Mode, Nomad, or other similar complex system to manage distributed containers on multiple machines, then you will probably want to **handle replication** at the **cluster level** instead of using a **process manager** in each container that starts multiple **worker processes**, which is what this Docker image does.

In those cases (e.g. using Kubernetes) you would probably want to build a **Docker image from scratch**, installing your dependencies, and running **a single process** instead of this image.

For example, using [Gunicorn](https://gunicorn.org/) you could have a file `app/gunicorn_conf.py` with:

```Python
# Gunicorn config variables
loglevel = "info"
errorlog = "-"  # stderr
accesslog = "-"  # stdout
worker_tmp_dir = "/dev/shm"
graceful_timeout = 120
timeout = 120
keepalive = 5
threads = 3
```

And then you could have a `Dockerfile` with:

```Dockerfile
FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["gunicorn", "--conf", "app/gunicorn_conf.py", "--bind", "0.0.0.0:80", "app.main:app"]
```

You can read more about these ideas in the [FastAPI documentation about: FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/#replication-number-of-processes) as the same ideas would apply to other web applications in containers.

[uWSGI is now in maintenance mode](https://uwsgi-docs.readthedocs.io/en/latest/), so it's probably better to migrate to a different tool.

Additionally, I haven't used this Docker image in years, so I don't have much bandwidth to keep it up to date. Most of my time is dedicated to [FastAPI](https://fastapi.tiangolo.com/) and friends.

You can probably still use this image as-is, while you migrate to a different tool, but I won't be adding (and maintaining) support for new versions of Python.

---

## Historical Docs

The rest of the README is preserved mainly for historical reasons.

## General Instructions

You don't have to clone this repo.

You can use this image as a base image for other images.

Assuming you have a file `requirements.txt`, you could have a `Dockerfile` like this:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.12

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
```

There are several image tags available but for new projects you should use the latest version available.

This Docker image is based on [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/). That Docker image has uWSGI and Nginx installed in the same container and was made to be the base of this image.

## Quick Start

* Go to your project directory
* Create a `Dockerfile` with:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.12

COPY ./app /app
```

* Create an `app` directory and enter in it
* Create a `main.py` file (it should be named like that and should be in your `app` directory) with:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
```

the main application object should be named `app` (in the code) as in this example.

**Note**: The section with the `main()` function is for debugging purposes. To learn more, read the **Advanced instructions** below.

* You should now have a directory structure like:

```
.
├── app
│   └── main.py
└── Dockerfile
```

* Go to the project directory (in where your `Dockerfile` is, containing your `app` directory)
* Build your Flask image:

```bash
docker build -t myimage .
```

* Run a container based on your image:

```bash
docker run -d --name mycontainer -p 80:80 myimage
```

...and you have an optimized Flask server in a Docker container.

You should be able to check it in your Docker container's URL, for example: <a href="http://192.168.99.100" target="_blank">http://192.168.99.100</a> or <a href="http://127.0.0.1" target="_blank">http://127.0.0.1</a>

## Quick Start for SPAs *

### Modern Single Page Applications

If you are building modern frontend applications (e.g. [Vue](https://vuejs.org/), [React](https://reactjs.org/), [Angular](https://angular.io/)) you would most probably be compiling a modern version of JavaScript (ES2015, TypeScript, etc) to a less modern, more compatible version.

If you want to serve your (compiled) frontend code by the same backend (Flask) Docker container, you would have to copy the code to the container after compiling it.

That means that you would need to have all the frontend tools installed on the building machine (it might be your computer, a remote server, etc).

That also means that you would have to, somehow, always remember to compile the frontend code right before building the Docker image.

And it might also mean that you could then have to add your compiled frontend code to your `git` repository (hopefully you are using Git already, or [learning how to use `git`](https://www.atlassian.com/git)).

Adding your compiled code to Git is a very bad idea for several reasons, some of those are:

* You don't have a single, ultimate source of truth (the source code).
* The compiled code might be stale, even when your source code is new, which might make you spend a lot of time debugging.
* You might run into a lot of code conflicts when interacting with multiple team members with different Git branches, and spend a lot of time solving irrelevant code conflicts in the compiled code.
    * This might also ruin automatic branch merging in pull requests from other team members.

For these reasons, it is not recommended that you serve your frontend code from the same backend (Flask) Docker container.

### Better alternative

There's a much better alternative to serving your frontend code from the same backend (Flask) Docker container.

You can have another Docker container with all the frontend tools installed (Node.js, etc) that:

* Takes your source frontend code.
* Compiles it and generates the final "distributable" frontend.
* Uses Docker "multi-stage builds" to copy that compiled code into a pure Nginx Docker image.
* The final frontend image only contains the compiled frontend code, directly from the source, but has the small size of an Nginx image, with all the performance from Nginx.

To learn the specifics of this process for the frontend building in Docker you can read:

* [React in Docker with Nginx, built with multi-stage Docker builds, including testing](https://medium.com/@tiangolo/react-in-docker-with-nginx-built-with-multi-stage-docker-builds-including-testing-8cc49d6ec305)
* [Angular in Docker with Nginx, supporting configurations / environments, built with multi-stage Docker builds and testing with Chrome Headless](https://medium.com/@tiangolo/angular-in-docker-with-nginx-supporting-environments-built-with-multi-stage-docker-builds-bb9f1724e984)

After having one backend (Flask) container and one frontend container, you need to serve both of them.

And you might want to serve them under the same domain, under a different path. For example, the backend (Flask) app at the path `/api` and the frontend at the "root" path `/`.

You can then use [Traefik](https://traefik.io/) to handle that.

And it can also automatically generate HTTPS certificates for your application using Let's Encrypt. All for free, in a very easy setup.

In this scenario, you would have 3 Docker containers:

* Backend (Flask)
* Frontend (Vue.js, Angular, React or any other)
* Traefik (load balancer, HTTPS)

## Quick Start for bigger projects structured as a Python package

You should be able to follow the same instructions as in the "**QuickStart**" section above, with some minor modifications:

* Instead of putting your code in the `app/` directory, put it in a directory `app/app/`.
* Add an empty file `__init__.py` inside of that `app/app/` directory.
* Add a file `uwsgi.ini` inside your `app/` directory (that is copied to `/app/uwsgi.ini` inside the container).
* In your `uwsgi.ini` file, add:

```ini
[uwsgi]
module = app.main
callable = app
```

The explanation of the `uwsgi.ini` is as follows:

* The module in where my Python web app lives is `app.main`. So, in the package `app` (`/app/app`), get the `main` module (`main.py`).
* The Flask web application is the `app` object (`app = Flask(__name__)`).

Your file structure would look like:

```
.
├── app
│   ├── app
│   │   ├── __init__.py
│   │   ├── main.py
│   └── uwsgi.ini
└── Dockerfile
```

...instead of:

```
.
├── app
│   ├── main.py
└── Dockerfile
```

If you are using static files in the same container, make sure the `STATIC_PATH` environment variable is set accordingly, for example to change the default value of `/app/static` to `/app/app/static` you could add this line to your `Dockerfile`:

```Dockerfile
ENV STATIC_PATH /app/app/static
```

...after that, everything should work as expected. All the other instructions would apply normally.

### Working with submodules

* After adding all your modules you could end up with a file structure similar to (taken from the example project):

```
.
├── app
│   ├── app
│   │   ├── api
│   │   │   ├── api.py
│   │   │   ├── endpoints
│   │   │   │   ├── __init__.py
│   │   │   │   └── user.py
│   │   │   ├── __init__.py
│   │   │   └── utils.py
│   │   ├── core
│   │   │   ├── app_setup.py
│   │   │   ├── database.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── models
│   │       ├── __init__.py
│   │       └── user.py
│   └── uwsgi.ini
└── Dockerfile
```

* Make sure you follow [the official docs while importing your modules](https://docs.python.org/3/tutorial/modules.html#intra-package-references):

* For example, if you are in `app/app/main.py` and want to import the module in `app/app/core/app_setup.py` you would write it like:

```python
from .core import app_setup
```

or

```python
from app.core import app_setup
```

* And if you are in `app/app/api/endpoints/user.py` and you want to import the `users` object from `app/app/core/database.py` you would write it like:

```python
from ...core.database import users
```

or

```python
from app.core.database import users
```

## Advanced instructions

You can customize several things using environment variables.

### Serve `index.html` directly

**Notice**: this technique is deprecated, as it can create several issues with modern frontend frameworks. For the details and better alternatives, read the section above.

Setting the environment variable `STATIC_INDEX` to be `1` you can configure Nginx to serve the file in the URL `/static/index.html` when requested for `/`.

That would improve speed as it would not involve uWSGI nor Python. Nginx would serve the file directly. To learn more follow the section above "**QuickStart for SPAs**".

For example, to enable it, you could add this to your `Dockerfile`:

```Dockerfile
ENV STATIC_INDEX 1
```

### Custom uWSGI process number

By default, the image starts with 2 uWSGI processes running. When the server is experiencing a high load, it creates up to 16 uWSGI processes to handle it on demand.

If you need to configure these numbers you can use environment variables.

The starting number of uWSGI processes is controlled by the variable `UWSGI_CHEAPER`, by default set to `2`.

The maximum number of uWSGI processes is controlled by the variable `UWSGI_PROCESSES`, by default set to `16`.

Have in mind that `UWSGI_CHEAPER` must be lower than `UWSGI_PROCESSES`.

So, if, for example, you need to start with 4 processes and grow to a maximum of 64, your `Dockerfile` could look like:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.12

ENV UWSGI_CHEAPER 4
ENV UWSGI_PROCESSES 64

COPY ./app /app
```

### Max upload file size

You can set a custom maximum upload file size using an environment variable `NGINX_MAX_UPLOAD`, by default it has a value of `0`, that allows unlimited upload file sizes. This differs from Nginx's default value of 1 MB. It's configured this way because that's the simplest experience an inexperienced developer in Nginx would expect.

For example, to have a maximum upload file size of 1 MB (Nginx's default) add a line in your `Dockerfile` with:

```Dockerfile
ENV NGINX_MAX_UPLOAD 1m
```

### Custom listen port

By default, the container made from this image will listen on port 80.

To change this behavior, set the `LISTEN_PORT` environment variable. You might also need to create the respective `EXPOSE` Docker instruction.

You can do that in your `Dockerfile`, it would look something like:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.12

ENV LISTEN_PORT 8080

EXPOSE 8080

COPY ./app /app
```

### Custom `uwsgi.ini` configurations

There is a default file in `/app/uwsgi.ini` with app specific configurations (on top of the global `uwsgi` configurations).

It only contains:

```ini
[uwsgi]
module = main
callable = app
```

* `module = main` refers to the file `main.py`.
* `callable = app` refers to the `Flask` "application", in the variable `app`.

---

You can customize `uwsgi` by replacing that file with your own, including all your configurations.

For example, to extend the default one above and enable threads, you could have a file:

```ini
[uwsgi]
module = main
callable = app
enable-threads = true
```

### Custom `uwsgi.ini` file location

You can override where the image should look for the app `uwsgi.ini` file using the environment variable `UWSGI_INI`.

With that you could change the default directory for your app from `/app` to something else, like `/application`.

For example, to make the image use the file in `/application/uwsgi.ini`, you could add this to your `Dockerfile`:

```Dockerfile
ENV UWSGI_INI /application/uwsgi.ini

COPY ./application /application
WORKDIR /application
```

**Note**: the `WORKDIR` is important, otherwise uWSGI will try to run the app in `/app`.

**Note**: you would also have to configure the `static` files path, read below.

### Custom `./static/` path

You can make Nginx use a custom directory path with the files to serve directly (without having uWSGI involved) with the environment variable `STATIC_PATH`.

For example, to make Nginx serve the static content using the files in `/app/custom_static/` you could add this to your `Dockerfile`:

```Dockerfile
ENV STATIC_PATH /app/custom_static
```

Then, when the browser asked for a file in, for example, http://example.com/static/index.html, Nginx would answer directly using a file in the path `/app/custom_static/index.html`.

**Note**: you would also have to configure Flask to use that as its `static` directory.

---

As another example, if you needed to put your application code in a different directory, you could configure Nginx to serve those static files from that different directory.

If you needed to have your static files in `/application/static/` you could add this to your `Dockerfile`:

```Dockerfile
ENV STATIC_PATH /application/static
```

### Custom `/static` URL

You can also make Nginx serve the static files in a different URL, for that, you can use the environment variable `STATIC_URL`.

For example, if you wanted to change the URL `/static` to `/content` you could add this to your `Dockerfile`:

```Dockerfile
ENV STATIC_URL /content
```

Then, when the browser asked for a file in, for example, http://example.com/content/index.html, Nginx would answer directly using a file in the path `/app/static/index.html`.

### Custom `/app/prestart.sh`

If you need to run anything before starting the app, you can add a file `prestart.sh` to the directory `/app`. The image will automatically detect and run it before starting everything.

For example, if you want to add Alembic SQL migrations (with SQLAlchemy), you could create a `./app/prestart.sh` file in your code directory (that will be copied by your `Dockerfile`) with:

```bash
#! /usr/bin/env bash

# Let the DB start
sleep 10;
# Run migrations
alembic upgrade head
```

and it would wait 10 seconds to give the database some time to start and then run that `alembic` command.

If you need to run a Python script before starting the app, you could make the `/app/prestart.sh` file run your Python script, with something like:

```bash
#! /usr/bin/env bash

# Run custom Python script before starting
python /app/my_custom_prestart_script.py
```

**Note**: The image uses `source` to run the script, so for example, environment variables would persist. If you don't understand the previous sentence, you probably don't need it.

### Custom Nginx processes number

By default, Nginx will start one "worker process".

If you want to set a different number of Nginx worker processes you can use the environment variable `NGINX_WORKER_PROCESSES`.

You can use a specific single number, e.g.:

```Dockerfile
ENV NGINX_WORKER_PROCESSES 2
```

or you can set it to the keyword `auto` and it will try to auto-detect the number of CPUs available and use that for the number of workers.

For example, using `auto`, your Dockerfile could look like:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.12

ENV NGINX_WORKER_PROCESSES auto

COPY ./app /app
```

### Custom Nginx maximum connections per worker

By default, Nginx will start with a maximum limit of 1024 connections per worker.

If you want to set a different number you can use the environment variable `NGINX_WORKER_CONNECTIONS`, e.g:

```Dockerfile
ENV NGINX_WORKER_CONNECTIONS 2048
```

It cannot exceed the current limit on the maximum number of open files. See how to configure it in the next section.

### Custom Nginx maximum open files

The number connections per Nginx worker cannot exceed the limit on the maximum number of open files.

You can change the limit of open files with the environment variable `NGINX_WORKER_OPEN_FILES`, e.g.:

```Dockerfile
ENV NGINX_WORKER_OPEN_FILES 2048
```

### Customizing Nginx additional configurations

If you need to configure Nginx further, you can add `*.conf` files to `/etc/nginx/conf.d/` in your `Dockerfile`.

Just have in mind that the default configurations are created during startup in a file at `/etc/nginx/conf.d/nginx.conf` and `/etc/nginx/conf.d/upload.conf`. So you shouldn't overwrite them. You should name your `*.conf` file with something different than `nginx.conf` or `upload.conf`, for example: `custom.conf`.

**Note**: if you are customizing Nginx, maybe copying configurations from a blog or a StackOverflow answer, have in mind that you probably need to use the [configurations specific to uWSGI](http://nginx.org/en/docs/http/ngx_http_uwsgi_module.html), instead of those for other modules, like for example, `ngx_http_fastcgi_module`.

### Overriding Nginx configuration completely

If you need to configure Nginx even further, completely overriding the defaults, you can add a custom Nginx configuration to `/app/nginx.conf`.

It will be copied to `/etc/nginx/nginx.conf` and used instead of the generated one.

Have in mind that, in that case, this image won't generate any of the Nginx configurations, it will only copy and use your configuration file.

That means that all the environment variables described above that are specific to Nginx won't be used.

It also means that it won't use additional configurations from files in `/etc/nginx/conf.d/*.conf`, unless you explicitly have a section in your custom file `/app/nginx.conf` with:

```conf
include /etc/nginx/conf.d/*.conf;
```

If you want to add a custom `/app/nginx.conf` file but don't know where to start from, you can use [the `nginx.conf` used for the tests](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/tests/test_02_app/custom_nginx_app/app/nginx.conf) and customize it or modify it further.

## Technical details

The combination of uWSGI with Nginx is a [common way to deploy Python Flask web applications](http://flask.pocoo.org/docs/1.0/deploying/uwsgi/).

Roughly:

* **Nginx** is a web server, it takes care of the HTTP connections and also can serve static files directly and more efficiently.

* **uWSGI** is an application server, that's what runs your Python code and it talks with Nginx.

* **Your Python code** has the actual **Flask** web application, and is run by uWSGI.

The image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) takes advantage of already existing slim and optimized Docker images (based on Debian as [recommended by Docker](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)) and implements several of Docker's best practices.

It uses the official Python Docker image, installs uWSGI and on top of that (with the least amount of modifications) adds the official Nginx image.

And it controls all these processes with Supervisord.

The image (and tags) created by this repo is based on the image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/). This image adds Flask and sensible defaults on top of it.

If you follow the instructions and keep the root directory `/app` in your container, with a file named `main.py` and a Flask object named `app` in it, it should "just work".

There's already a `uwsgi.ini` file in the `/app` directory with the uWSGI configurations for it to "just work". And all the other required parameters are in another `uwsgi.ini` file in the image, inside `/etc/uwsgi/`.

If you need to change the main file name or the main Flask object, you would have to provide your own `uwsgi.ini` file. You may use the one in this repo as a template to start with (and you only would have to change the 2 corresponding lines).

You can have a `/app/static` directory and those files will be efficiently served by Nginx directly (without going through your Flask code or even uWSGI), it's already configured for you. But you can configure it further using environment variables (read above).

Supervisord takes care of running uWSGI with the `uwsgi.ini` file in `/app` file (including also the file in `/etc/uwsgi/uwsgi.ini`) and starting Nginx.

---

There's the rule of thumb that you should have "one process per container".

That helps, for example, isolating an app and its database in different containers.

But if you want to have a "micro-services" approach you may want to [have more than one process in one container](https://valdhaus.co/writings/docker-misconceptions/) if they are all related to the same "service", and you may want to include your Flask code, uWSGI and Nginx in the same container (and maybe run another container with your database).

That's the approach taken in this image.

---

This image (and tags) have some default files, so if you run it by itself (not as the base image of your own project) you will see a default "Hello World" web app.

When you build a `Dockerfile` with a `COPY ./app /app` you replace those default files with your app code.

The main default file is only in `/app/main.py`. And in the case of the tags with `-index`, also in `/app/static/index.html`.

But those files render a "(default)" text in the served web page, so that you can check if you are seeing the default code or your own code overriding the default.

Your app code should be in the container's `/app` directory, it should have a `main.py` file and that `main.py` file should have a Flask object `app`.

If you follow the instructions above or use one of the downloadable example templates, you should be OK.

There is also a `/app/uwsgi.ini` file inside the images with the default parameters for uWSGI.

The downloadable examples include a copy of the same `uwsgi.ini` file for debugging purposes. To learn more, read the "**Advanced development instructions**" below.

## Advanced development instructions

While developing, you might want to make your code directory a volume in your Docker container.

With that you would have your files (temporarily) updated every time you modify them, without needing to build your container again.

To do this, you can use the command `pwd` (print working directory) inside your `docker run` and the flag `-v` for volumes.

With that you could map your `./app` directory to your container's `/app` directory.

But first, as you will be completely replacing the directory `/app` in your container (and all of its contents) you will need to have a `uwsgi.ini` file in your `./app` directory with:

```ini
[uwsgi]
module = main
callable = app
```

and then you can do the Docker volume mapping.

**Note**: A `uwsgi.ini` file is included in the downloadable examples.

* To try it, go to your project directory (the one with your `Dockerfile` and your `./app` directory)
* Make sure you have a `uwsgi.ini` file in your `./app` directory
* Build your Docker image:

```bash
docker build -t myimage .
```

* Run a container based on your image, mapping your code directory (`./app`) to your container's `/app` directory:

```bash
docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app myimage
```

If you go to your Docker container URL you should see your app, and you should be able to modify files in `./app/static/` and see those changes reflected in your browser just by reloading.

...but, as uWSGI loads your whole Python Flask web application once it starts, you won't be able to edit your Python Flask code and see the changes reflected.

To be able to (temporarily) debug your Python Flask code live, you can run your container overriding the default command (that starts Supervisord which in turn starts uWSGI and Nginx) and run your application directly with `python`, in debug mode, using the `flask` command with its environment variables.

So, with all the modifications above and making your app run directly with `flask`, the final Docker command would be:

 ```bash
docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app -e FLASK_APP=main.py -e FLASK_DEBUG=1 myimage flask run --host=0.0.0.0 --port=80
```

Or in the case of a package project, you would set `FLASK_APP=main/main.py`:

```bash
docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app -e FLASK_APP=main/main.py -e FLASK_DEBUG=1 myimage flask run --host=0.0.0.0 --port=80
```

Now you can edit your Flask code in your local machine and once you refresh your browser, you will see the changes live.

Remember that you should use this only for debugging and development, for deployment in production you shouldn't mount volumes and you should let Supervisord start and let it start uWSGI and Nginx (which is what happens by default).

An alternative for these last steps to work when you don't have a package, but just a flat structure with single files (modules), your Python Flask code could have that section with:

```python
if __name__ == "__main__":
   # Only for debugging while developing
   app.run(host='0.0.0.0', debug=True, port=80)
```

...and you could run it with `python main.py`. But that will only work when you are not using a package structure and don't plan to do it later. In that specific case, if you didn't add the code block above, your app would only listen to `localhost` (inside the container), in another port (5000) and not in debug mode.

---

Also, if you want to do the same live debugging using the environment variable `STATIC_INDEX=1` (to serve `/app/static/index.html` directly when requested for `/`) your Nginx won't serve it directly as it won't be running (only your Python Flask app in debug mode will be running).

```python
from flask import Flask, send_file
```

and

```python
@app.route('/')
def route_root():
    index_path = os.path.join(app.static_folder, 'index.html')
    return send_file(index_path)
```

...that makes sure your app also serves the `/app/static/index.html` file when requested for `/`. Or if you are using a package structure, the `/app/main/static/index.html` file.

And if you are using a SPA framework, to allow it to handle the URLs in the browser, your Python Flask code should have the section with:

```python
# Everything not declared before (not a Flask route / API endpoint)...
@app.route('/<path:path>')
def route_frontend(path):
    # ...could be a static file needed by the front end that
    # doesn't use the `static` path (like in `<script src="bundle.js">`)
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return send_file(file_path)
    # ...or should be handled by the SPA's "router" in front end
    else:
        index_path = os.path.join(app.static_folder, 'index.html')
        return send_file(index_path)
```

...that makes Flask send all the CSS, JavaScript and image files when requested in the root (`/`) URL but also makes sure that your frontend SPA handles all the other URLs that are not defined in your Flask app.

That's how it is written in the tutorial above and is included in the downloadable examples.

## More advanced development instructions

If you follow the instructions above, it's probable that at some point, you will write code that will break your Flask debugging server and it will crash.

And since the only process running was your debugging server, that now is stopped, your container will stop.

Then you will have to start your container again after fixing your code and you won't see very easily what is the error that is crashing your server.

So, while developing, you could do the following (that's what I normally do, although I do it with Docker Compose, as in the example projects):

* Make your container run and keep it alive in an infinite loop (without running any server):

```bash
docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app -e FLASK_APP=main.py -e FLASK_DEBUG=1 myimage bash -c "while true ; do sleep 10 ; done"
```

* Or, if your project is a package, set `FLASK_APP=main/main.py`:

```bash
docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app -e FLASK_APP=main/main.py -e FLASK_DEBUG=1 myimage bash -c "while true ; do sleep 10 ; done"
```

* Connect to your container with a new interactive session:

```bash
docker exec -it mycontainer bash
```

You will now be inside your container in the `/app` directory.

* Now, from inside the container, run your Flask debugging server:

```bash
flask run --host=0.0.0.0 --port=80
```

You will see your Flask debugging server start, you will see how it sends responses to every request, you will see the errors thrown when you break your code, and how they stop your server, and you will be able to re-start it very fast, by just running the command above again.

## Tests

All the image tags, configurations, environment variables and application options are tested.

## License

This project is licensed under the terms of the Apache license.
