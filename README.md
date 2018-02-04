## Supported tags and respective `Dockerfile` links

* [`python3.6` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python3.6/Dockerfile)
* [`python3.6-index` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python3.6-index/Dockerfile)
* [`python3.6-alpine3.7` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python3.6-alpine3.7/Dockerfile)
* [`python3.5` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python3.5/Dockerfile)
* [`python3.5-index` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python3.5/Dockerfile)
* [`python2.7` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python2.7/Dockerfile)
* [`python2.7-index` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python2.7-index/Dockerfile)
* [`python2.7-alpine3.7` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python2.7-alpine3.7/Dockerfile)


## DEPRECATED tags and respective `Dockerfile` links

* [`flask`, `flask-upload`, `latest` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/deprecated/Dockerfile)
* [`flask-index`, `flask-index-upload` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/deprecated-index/Dockerfile)
* [`flask-python3.5`, `flask-python3.5-upload`  _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python3.5/Dockerfile)
* [`flask-python3.5-index`, `flask-python3.5-index-upload`  _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python3.5-index/Dockerfile)
* [`flask-python2.7` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python2.7/Dockerfile)


# uwsgi-nginx-flask

**Docker** image with **uWSGI** and **Nginx** for **Flask** web applications in **Python 3.6**, **Python 3.5** and **Python 2.7** running in a single container. Optionally using Alpine Linux.

## Description

This [**Docker**](https://www.docker.com/) image allows you to create [**Flask**](http://flask.pocoo.org/) web applications in [**Python**](https://www.python.org/) that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/) in a single container.

uWSGI with Nginx is one of the best ways to deploy a Python web application, so you you should have a [good performance (check the benchmarks)](http://nichol.as/benchmark-of-python-web-servers) with this image.

There is also an Alpine version. If you want it, use one of the Alpine tags from above.

**GitHub repo**: <https://github.com/tiangolo/uwsgi-nginx-flask-docker>

**Docker Hub image**: <https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/>

## Examples (project templates)

* **`python3.6`** tag: general Flask web application: 

[**example-flask-python3.6.zip**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.3.5/example-flask-python3.6.zip>)

* **`python3.6`** tag: general Flask web application, structured as a package, for bigger Flask projects, with different submodules. Use it only as an example of how to import your modules and how to structure your own project:

[**example-flask-package-python3.6.zip**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.3.5/example-flask-package-python3.6.zip>)

* **`python3.6-index`** tag: `static/index.html` served directly in `/`, e.g. for Angular, React, or any other Single-Page Application that uses a static `index.html`, not modified by Python: 

[**example-flask-python3.6-index.zip**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.3.5/example-flask-python3.6-index.zip>)

## General Instructions

You don't have to clone this repo, you should be able to use this image as a base image for your project with something in your `Dockerfile` like:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app /app
```

There are several image tags available for Python 3.6, Python 3.5 and Python 2.7, but for new projects you should use **Python 3.6**. 

As of now, [everyone](https://www.python.org/dev/peps/pep-0373/) [should be](http://flask.pocoo.org/docs/0.12/python3/#python3-support) [using **Python 3**](https://docs.djangoproject.com/en/1.11/faq/install/#what-python-version-should-i-use-with-django).

There are several template projects that you can download (as a `.zip` file) to bootstrap your project in the section "**Examples (project templates)**" above.

This Docker image is based on [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/). That Docker image has uWSGI and Nginx installed in the same container and was made to be the base of this image.


## QuickStart

**Note**: You can download the **example-flask-python3.6.zip** project example and use it as the template for your project from the section **Examples** above.

---

Or you may follow the instructions to build your project from scratch:

* Go to your project directory
* Create a `Dockerfile` with:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.6

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

You should be able to check it in your Docker container's URL, for example: <http://192.168.99.100/>


## QuickStart for SPAs

This section explains how to configure the image to serve the contents of `/static/index.html` directly when the browser requests `/`.

This is specially helpful (and efficient) if you are building a Single-Page Application (SPA) with JavaScript (Angular, React, etc) and you want the `index.html` to be served directly, without modifications by Python or Jinja2 templates. And you want to use Flask mainly as an API / back end for your SPA front end.

**Note**: You can download the example project **example-flask-python3.6-index.zip** and use it as the template for your project in the **Examples** section above.

---

Or you may follow the instructions to build your project from scratch (it's very similar to the procedure above):

* Go to your project directory
* Create a `Dockerfile` with:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_INDEX 1

COPY ./app /app
```

* Create an `app` directory and enter in it
* Create a `main.py` file (it should be named like that and should be in your `app` directory) with:

```python
from flask import Flask, send_file
app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World from Flask"


@app.route("/")
def main():
    index_path = os.path.join(app.static_folder, 'index.html')
    return send_file(index_path)


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


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
```

the main application object should be named `app` (in the code) as in this example.

**Note**: The section with the `main()` function is for debugging purposes. To learn more, read the **Advanced instructions** below.

* Make sure you have an `index.html` file in `./app/static/index.html`, for example with:

```html
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

* You should now have a directory structure like:

```
.
├── app
│   ├── main.py
│   └── static
│       └── index.html
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

...and you have an optimized Flask server in a Docker container. Also optimized to serve your main static `index.html` page.

* Now, when you go to your Docker container URL, for example: <http://192.168.99.100/>, you will see your `index.html` as if you were in <http://192.168.99.100/static/index.html>.

* You should be able to also go to, for example, <http://192.168.99.100/hello> to see a "Hello World" page served by Flask.

**Note**: As your `index.html` file will be served from `/` and from `/static/index.html`, it would be better to have absolute paths in the links to other files in the `static` directory from your `index.html` file. As in `/static/css/styles.css` instead of relative paths as in `./css/styles.css`. But still, above you added code in your `main.py` to handle that too, just in case.

## QuickStart for bigger projects structured as a Python package

**Note**: You can download the **example-flask-package-python3.6.zip** project example and use it as an example or template for your project from the section **Examples** above.

---

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

* Make sure you follow [the offical docs while importing your modules](https://docs.python.org/3/tutorial/modules.html#intra-package-references):

* For example, if you are in `app/app/main.py` and want to import the module in `app/app/core/app_setup.py` you would wirte it like:

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

Setting the environment variable `STATIC_INDEX` to be `1` you can configure Nginx to serve the file in the URL `/static/index.html` when requested for `/`. 

That would improve speed as it would not involve uWSGI nor Python. Nginx would serve the file directly. To learn more follow the section above "**QuickStart for SPAs**".

For example, to enable it, you could add this to your `Dockerfile`:

```Dockerfile
ENV STATIC_INDEX 1
```

### Max upload file size

You can set a custom maximum upload file size using an environment variable `NGINX_MAX_UPLOAD`, by default it has a value of `0`, that allows unlimited upload file sizes. This differs from Nginx's default value of 1 MB. It's configured this way because that's the simplest experience a developer that is not expert in Nginx would expect.

For example, to have a maximum upload file size of 1 MB (Nginx's default) add a line in your `Dockerfile` with:

```Dockerfile
ENV NGINX_MAX_UPLOAD 1m
```

### Custom listen port

By default, the container made from this image will listen on port 80.

To change this behavior, set the `LISTEN_PORT` environment variable. You might also need to create the respective `EXPOSE` Docker instruction.

You can do that in your `Dockerfile`, it would look something like:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV LISTEN_PORT 8080

EXPOSE 8080

COPY ./app /app
```

### Custom `uwsgi.ini` file

You can override where the image should look for the app `uwsgi.ini` file using the envirnoment variable `UWSGI_INI`.

With that you could change the default directory for your app from `/app` to something else, like `/application`.

For example, to make the image use the file in `/application/uwsgi.ini`, you could add this to your `Dockerfile`:

```Dockerfile
ENV UWSGI_INI /application/uwsgi.ini

COPY ./application /application
WORKDIR /application
```

**Note**: the `WORKDIR` is important, otherwhise uWSGI will try to run the app in `/app`.

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

For example, if you want to add Alembic SQL migrations (with SQLALchemy), you could create a `./app/prestart.sh` file in your code directory (that will be copied by your `Dockerfile`) with:

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
python /app/my_custom_prestart_script.y
```

**Note**: The image uses `source` to run the script, so for example, environment variables would persist. If you don't understand the previous sentence, you probably don't need it.

## Custom Nginx processes number

By default, Nginx will start one "worker process".

If you want to set a different number of Nginx worker processes you can use the environment variable `NGINX_WORKER_PROCESSES`.

You can use a specific single number, e.g.:

```Dockerfile
ENV NGINX_WORKER_PROCESSES 2
```

or you can set it to the keyword `auto` and it will try to autodetect the number of CPUs available and use that for the number of workers.

For example, using `auto`, your Dockerfile could look like:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV NGINX_WORKER_PROCESSES auto

COPY ./app /app
```

## Customizing Nginx configurations

If you need to configure Nginx further, you can add `*.conf` files to `/etc/nginx/conf.d/` in your Dockerfile.

Just have in mind that the default configurations are created during startup in a file in `/etc/nginx/conf.d/nginx.conf` and `/etc/nginx/conf.d/upload.conf`. So you shouldn't overwrite them. You should name your `*.conf` file with something different than `nginx.conf` or `upload.conf`.

## Technical details

One of the best ways to deploy a Python web application is with uWSGI and Nginx, as seen in the [benchmarks](http://nichol.as/benchmark-of-python-web-servers).

Roughly:

* **Nginx** is a web server, it takes care of the HTTP connections and also can serve static files directly and more efficiently.

* **uWSGI** is an application server, that's what runs your Python code and it talks with Nginx.

* **Your Python code** has the actual **Flask** web application, and is run by uWSGI.

The image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) takes advantage of already slim and optimized existing Docker images (based on Debian as [recommended by Docker](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)) and implements Docker best practices.

It uses the official Python Docker image, installs uWSGI and on top of that (with the least amount of modifications) and adds the official Nginx image.

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
bash
```
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

An alternative for these last steps to work when you don't have a package but just a flat structure with single files (modules), your Python Flask code could have that section with:

```python
if __name__ == "__main__":
   # Only for debugging while developing
   app.run(host='0.0.0.0', debug=True, port=80)
```

...and you could run it with `python main.py`. But that will only work when you are not using a package structure and don't plan to do it later. In that specific case, if you didn't add the code block above, your app would only listen to `localhost` (inside the container), in another port (5000) and not in debug mode.

**Note**: The example project **example-flask-python3.6** includes a `docker-compose.yml` and `docker-compose.override.yml` with all these configurations, if you are using Docker Compose.

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

...that makes Flask send all the CSS, JavaScript and image files when requested in the root (`/`) URL but also makes sure that your front end SPA handles all the other URLs that are not defined in your Flask app.

That's how it is written in the tutorial above and is included in the downloadable examples.

**Note**: The example project **example-flask-python3.6-index** includes a `docker-compose.yml` and `docker-compose.override.yml` with all these configurations, if you are using Docker Compose.

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

You will see your Flask debugging server start, you will see how it sends responses to every request, you will see the errors thrown when you break your code and how they stop your server and you will be able to re-start your server very fast, by just running the command above again.

## What's new

2018-02-04:

It's now possible to set the number of Nginx worker processes with the environment variable `NGINX_WORKER_PROCESSES`. Thanks to [naktinis](https://github.com/naktinis) in [this PR](https://github.com/tiangolo/uwsgi-nginx-docker/pull/22).

2018-01-14:

* There are now two Alpine based versions, `python2.7-alpine3.7` and `python3.6-alpine3.7`.

2017-12-10: 

* Added support for `/app/prestart.sh` script to run arbitrary code before starting the app (for example, Alembic - SQLAlchemy migrations). The [documentation for the `/app/prestart.sh` is in the main README](https://github.com/tiangolo/uwsgi-nginx-flask-docker#custom-appprestartsh).
* `/app` is part of the `PYTHONPATH` environment variable. That allows global imports from several places, easier Alembic integration, etc.

2017-12-08: Now you can configure which port the container should listen on, using the environment variable `LISTEN_PORT` thanks to [tmshn](https://github.com/tmshn) in [this PR](https://github.com/tiangolo/uwsgi-nginx-docker/pull/16).

2017-09-10: Updated examples and sample project to work with SPAs even when structuring the app as a package (with subdirectories).

2017-09-02: 

* Example project with a [Python package](https://docs.python.org/3/tutorial/modules.html#packages) structure and a section explaining how to use it and structure a Flask project like that. 
* Also, the examples and documentation now use the [`flask run`](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application) commands, that allows running a package application while developing more easily.

2017-08-10: Many changes:

* New official image tags: `python3.6`, `python3.6-index`, `python.3.5`, `python3.5-index`, `python2.7` and `python2.7-index`. All the other images are deprecated in favor is this ones. 
* Python 3.6 is now the recommended default. Even the example projects for other versions were removed to discourage using older Python versions for new projects.
* Any of the older images that didn't have a Python version will show a deprecation warning and take some time to start. As soon the tag `latest` will point to Python 3.6 and the other tags will be removed.
* There were several improvements in the bas image `tiangolo/uwsgi-nginx` that improved this image too.
* By default, now there is no limit in the upload file size in Nginx. It can be configured in an environment variable.
* It's now possible to configure several things with environment variables: 
  * Serve `index.html` directly: `STATIC_INDEX`
  * Set the max upload file size: `NGINX_MAX_UPLOAD`
  * Set a custom `uwsgi.ini` file (that allows using a custom directory different than `/app`): `UWSGI_INI` (using the ideas by @bercikr in #5 ).
  * Set a custom `./static/` path: `STATIC_PATH`
  * Set a custom `/static/` URL: `STATIC_URL`
* As all this configurations are available as environment variables, the choices are a lot more simple. Actually, any new project would just need to use a `Dockerfile` with:

```Dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app /app
```

and then customize with environment variables.



## License

This project is licensed under the terms of the Apache license.
