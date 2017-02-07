## Supported tags and respective `Dockerfile` links

* [`flask`, `flask-python2.7`, `latest` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/flask/Dockerfile)
* [`flask-index` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/flask-index/Dockerfile)
* [`flask-upload` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/flask-upload/Dockerfile)
* [`flask-index-upload` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/flask-index-upload/Dockerfile)
* [`flask-python3.5` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/flask-python3.5/Dockerfile)
* [`flask-python3.5-index` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/flask-python3.5-index/Dockerfile)
* [`flask-python3.5-upload` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/flask-python3.5-upload/Dockerfile)
* [`flask-python3.5-index-upload` _(Dockerfile)_](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/flask-python3.5-index-upload/Dockerfile)

# uwsgi-nginx-flask

**Docker** image with **uWSGI** and **Nginx** for **Flask** web applications in **Python 2.7** and **Python 3.5** running in a single container.

## Description

This [**Docker**](https://www.docker.com/) image allows you to create [**Flask**](http://flask.pocoo.org/) web applications in [**Python**](https://www.python.org/) that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/) in a single container.

uWSGI with Nginx is one of the best ways to deploy a Python web application, so you you should have a [good performance (check the benchmarks)](http://nichol.as/benchmark-of-python-web-servers) with this image.

**GitHub repo**: <https://github.com/tiangolo/uwsgi-nginx-flask-docker>

**Docker Hub image**: <https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/>

## Examples (project templates)

* **`flask`** tag (general Flask web application): [**example-flask**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.2.0/example-flask.zip>)

  * *`flask-python3.5`* tag (the equivalent as above, using Python 3.5): [**example-flask-python3.5**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.2.0/example-flask-python3.5.zip>)

* **`flask-upload`** tag (general Flask web application. Allowing uploads of up to 100 MB.): [**example-flask-upload**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.2.0/example-flask-upload.zip>)

  * *`flask-python3.5-upload`* tag (the equivalent as above, using Python 3.5): [**example-flask-python3.5-upload**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.2.0/example-flask-python3.5-upload.zip>)

* **`flask-index`** tag (`static/index.html` served directly in `/`, e.g. for Angular JS): [**example-flask-index**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.2.0/example-flask-index.zip>)

  * *`flask-python3.5-index`* tag (the equivalent as above, using Python 3.5): [**example-flask-python3.5-index**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.2.0/example-flask-python3.5-index.zip>)

* **`flask-index-upload`** tag (`static/index.html` served directly in `/`, e.g. for Angular JS. Allowing uploads of up to 100 MB.): [**example-flask-index-upload**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.2.0/example-flask-index-upload.zip>)

  * *`flask-python3.5-index-upload`* tag (the equivalent as above, using Python 3.5): [**example-flask-python3.5-index-upload**](<https://github.com/tiangolo/uwsgi-nginx-flask-docker/releases/download/v0.2.0/example-flask-python3.5-index-upload.zip>)

## General Instructions

You don't have to clone this repo, you should be able to use this image as a base image for your project.

There are several image tags, for each one, there's a template repo (a `.zip` file that you can download from above, in the "**Examples**" section):

* **`flask`** (also `latest` and `flask-python2.7`): An image based on the [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) image. This image includes Flask and a sample app.

The image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) has uWSGI and Nginx installed in the same container and is made to be the base of this image.

Use `FROM tiangolo/uwsgi-nginx-flask:flask` in your `Dockerfile` to use this image. (This would be the most general purpose tag image).

* **`flask-upload`**: The same as **`flask`** but configuring Nginx to allow uploads of up to 100 MB (the default is 1 MB).

Use `FROM tiangolo/uwsgi-nginx-flask:flask-upload` in your `Dockerfile` to use this image. (This would be the most general purpose tag image).

* **`flask-index`**: An image based on the **`flask`** image (above), but optimizing the configuration to make Nginx serve `/app/static/index.html` directly (instead of going through uWSGI and your code) when requested for `/`.

This is specially helpful (and efficient) if you are building a single-page app without Jinja2 templates (as with Angular JS) and using Flask as an API / back-end.

Use `FROM tiangolo/uwsgi-nginx-flask:flask-index` in your `Dockerfile` to use this image.

* **`flask-index-upload`**: The same as **`flask-index`** but configuring Nginx to allow uploads of up to 100 MB (the default is 1 MB).

Use `FROM tiangolo/uwsgi-nginx-flask:flask-index-upload` in your `Dockerfile` to use this image. (This would be the most general purpose tag image).

* **Python 3.5**: There is a version of all the images and example templates above using Python 3.5. The usage is very similiar to the usage of the normal (Python 2.7) version, but using the equivalent `python3.5` tag (you can see all the available tags on the top). Nevertheless, [Python 2.7 is still the default as the Flask maintainers use it as default and port the code to Python 3.5](http://flask.pocoo.org/docs/0.11/python3/) and Python 2.7 is still the most used and supported version.

## Creating a Flask project with Docker

**Note**: These instructions are for the `flask` tag and are intended for a general purpose Flask web application.

You can download the **example-flask** project example and use it as the template for your project from the section **Examples** above.

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

You can download the example project **example-flask-index** and use it as the template for your project in the **Examples** section above.

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

**Note**: As your `index.html` file will be served from `/` and from `/static/index.html`, the links to other files in the `static` directory from your `index.html` file should be absolute, as in `/static/css/styles.css` instead of relative as in `./css/styles.css`.

## Customizing Nginx configurations

If you only need to configure Nginx to allow uploads of up to 100 MB, you can use one of the example projects from the **Examples** section above:

* **example-flask-upload**: With the Docker image tag `flask-upload`, for general purpose Flask web applications with uploads of up to 100 MB (instead of the default 1 MB).

* **example-flask-index-upload**: With the Docker image tag `flask-index-upload`, for Flask web applications that serve `/static/index.html` directly when requested for `/` (useful with Angular JS) and with uploads of up to 100 MB (instead of the default 1 MB).

---

If you need to customize your Nginx configuration, you can copy `*.conf` files to `/etc/nginx/conf.d/` in your Dockerfile.

For example:

* Let's imagine you need to set the maximum upload file size to 50 MB, you can then create a file `my_upload_max.conf` with the contents:

```
client_max_body_size 50m;
```

* And in your Dockerfile, you can copy that file to the Nginx configurations directory:

```
FROM tiangolo/uwsgi-nginx-flask:flask

COPY ./my_upload_max.conf /etc/nginx/conf.d/

COPY ./app /app
```

And that's it. Just have in mind that the basic image tags (`flask` and `flask-index`) add their configurations in a file in `/etc/nginx/conf.d/nginx.conf`. So you shouldn't overwrite it. You should name your `*.conf` file with something different than `nginx.conf`.

## Technical details

One of the best ways to deploy a Python web application is with uWSGI and Nginx, as seen in the [benchmarks](http://nichol.as/benchmark-of-python-web-servers).

Roughly:

* **Nginx** is a web server, it takes care of the HTTP connections and also can serve static files directly and more efficiently.

* **uWSGI** is an application server, that's what runs your Python code and it talks with Nginx.

* **Your Python code** has the actual **Flask** web application, and is run by uWSGI.

The image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) takes advantage of already slim and optimized existing Docker images (based on Debian as [recommended by Docker](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)) and implements Docker best practices.

It uses the official Python Docker image, installs uWSGI and on top of that, with the least amount of modifications, adds the official Nginx image (as of 2016-02-14).

And it controls all these processes with Supervisord.

The image (and tags) created by this repo is based on the image [**tiangolo/uwsgi-nginx**](https://hub.docker.com/r/tiangolo/uwsgi-nginx/) and adds Flask and sensible defaults on top of it.

If you follow the instructions and keep the root directory `/app` in your container, with a file named `main.py` and a Flask object named `app` in it, it should "just work".

There's already a `uwsgi.ini` file in the `/app` directory with the uWSGI configurations for it to "just work". And even all the other required parameters are in another `uwsgi.ini` file in the image, inside `/etc/uwsgi/`.

If you need to change the main file name or the main Flask object, you would have to provide your own `uwsgi.ini` file. You may use the one in this repo as a template to start with (and you only would have to change the 2 corresponding lines).

You can have a `/app/static` directory and those files will be efficiently served by Nginx directly (without going through your Flask code or even uWSGI), it's already configured for you.

Supervisord takes care of running uWSGI with the `uwsgi.ini` file in `/app` file (including also the file in `/etc/uwsgi/uwsgi.ini`) and starting Nginx.

---

There's the rule of thumb that you should have "one process per container".

That helps, for example, isolating an app and its database in different containers.

But if you want to have a "micro-services" approach you may want to [have more than one process in one container](https://valdhaus.co/writings/docker-misconceptions/) if they are all related to the same "service", and you may want to include your Flask code, uWSGI and Nginx in the same container (and maybe run another container with your database).

That's the approach taken in this image.

---

This image (and tags) have some default files, so if you run it by itself (not as the base image of your own project) you will see a default "Hello World" web app.

When you build a `Dockerfile` with a `COPY ./app /app` you replace those default files with your app code.

The main default file is only in `/app/main.py`. And in the case of the tag `flask-index`, also in `/app/static/index.html`.

But those files render a "(default)" text in the served web page, so that you can check if you are seeing the default code or your own code overriding the default.

Your app code should be in the container's `/app` directory, it should have a `main.py` file and that `main.py` file should have a Flask object `app`.

If you follow the instructions above or use one of the downloadable example templates, you should be OK.

There is also a `/app/uwsgi.ini` file inside the images with the default parameters for uWSGI.

In the downloadable examples is a copy of the same `uwsgi.ini` file for debugging purposes. To learn more, read the **Advanced instructions** below.

## Advanced development instructions

While developing, you might want to make your code directory a volume in your Docker container.

With that you would have your files (temporarily) updated every time you modify them, without needing to build your container again.

To do this, you can use the command `pwd` (print working directory) inside your `docker run` and the flag `-v` for volumes.

With that you could map your `./app` directory to your container's `/app` directory.

But first, as you will be completely replacing the directory `/app` in your container (and all of its contents) you will need to have a `uwsgi.ini` file in your `./app` directory with:

```
[uwsgi]
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

If you go to your Docker container URL you should see your app, and you should be able to modify files in `./app/static/` and see those changes reflected in your browser just by reloading.

...but, as uWSGI loads your whole Python Flask web application once it starts, you won't be able to edit your Python Flask code and see the changes reflected.

To be able to (temporarily) debug your Python Flask code live, you can run your container overriding the default command (that starts Supervisord which in turn starts uWSGI and Nginx) and run your application directly with `python`, in debug mode.

So, with all the modifications above and making your app run directly with `python`, the final Docker command would be:

 ```
docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app myimage python /app/main.py
```

Now you can edit your Flask code in your local machine and once you refresh your browser, you will see the changes live.

Remember that you should use this only for debugging and development, for deployment in production you shouldn't mount volumes and you should let Supervisord start and let it start uWSGI and Nginx (which is what happens by default).

For these last steps to work (live debugging and development), your Python Flask code should have that section with:

 ```
 if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
 ```

otherwise your app will only listen to localhost (inside the container) and in another port (5000) and not in debug mode.

---

Also, if you want to do the same live debugging using the `flask-index` tag (to serve `/app/static/index.html` directly when requested for `/`) your Nginx won't serve it directly as it won't be running (only your Python Flask app in debug mode will be running).

For that, your Python Flask code should have that section with:

```
from flask import Flask, send_file
```

and

```
@app.route("/")
def main():
    return send_file('./static/index.html')
```

That makes sure your app also serves the `/app/static/index.html` file when requested for `/`.

 That's how it is written in the tutorial above and is included in the downloadable examples.

## More advanced development instructions

If you follow the instructions above, it's probable that at some point, you will write code that will break your Flask debugging server and it will crash.

And since the only process running was your debugging server, that now is stopped, your container will stop.

Then you will have to start your container again after fixing your code and you won't see very easily what is the error that is crashing your server.

So, while developing, you could do the following (that's what I normally do):

* Make your container run and keep it alive in an infinite loop (without running any server):

```
docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app myimage bash -c "while true ; do sleep 10 ; done"
```

* Connect to your container with a new interactive session:

```
docker exec -it mycontainer bash
```

You will now be inside your container in the `/app` directory.

* Now, from inside the container, run your Flask debugging server:

```
python main.py
```

You will see your Flask debugging server start, you will see how it sends responses to every request, you will see the errors thrown when you break your code and how they stop your server and you will be able to re-start your server very fast, by just running the command above again.

## Working Outside of the /app Directory
If for any reason you wish to run your application outside of the /app directory you may do so by using the following instructions.

Add the following file to your project (in the same directory as Dockerfile) 

* filename: `supervisord.conf`

```
[supervisord]
nodaemon=true

[program:uwsgi]
command=/usr/local/bin/uwsgi --ini /etc/uwsgi/uwsgi.ini
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0

[program:nginx]
command=/usr/sbin/nginx
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
```

then add the following lines to the bottom of your Dockerfile
```
# Copy the supervisord.conf which contains the application path to correct location
COPY ./supervisord.conf /etc/supervisor/conf.d/

# Set the environment variables to configure uWSGI to find the right app to start
ENV UWSGI_INI=<YOUR_APP_FOLDER>/uwsgi.ini
WORKDIR <YOUR_APP_FOLDER>
```


## License

This project is licensed under the terms of the Apache license.
