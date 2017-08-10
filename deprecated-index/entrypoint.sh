#!/bin/bash
set -e
# Get the maximum upload file size for Nginx, default to 0: unlimited
USE_NGINX_MAX_UPLOAD=${NGINX_MAX_UPLOAD:-0}
# Generate Nginx config for maximum upload file size
echo "client_max_body_size $USE_NGINX_MAX_UPLOAD;" > /etc/nginx/conf.d/upload.conf

# Get the URL for static files from the environment variable
USE_STATIC_URL=${STATIC_URL:-'/static'}
# Get the absolute path of the static files from the environment variable
USE_STATIC_PATH=${STATIC_PATH:-'/app/static'}

# Generate Nginx config first part using the environment variables
echo 'server {
    location / {
        try_files $uri @app;
    }
    location @app {
        include uwsgi_params;
        uwsgi_pass unix:///tmp/uwsgi.sock;
    }
    '"location $USE_STATIC_URL {
        alias $USE_STATIC_PATH;
    }" > /etc/nginx/conf.d/nginx.conf

# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
if [[ $STATIC_INDEX == 1 ]] ; then 
echo "    location = / {
        index $USE_STATIC_URL/index.html;
    }" >> /etc/nginx/conf.d/nginx.conf
fi
# Finish the Nginx config file
echo "}" >> /etc/nginx/conf.d/nginx.conf


echo -e "WARNING: YOU SHOULDN'T BE USING THIS DOCKER TAG.

These Docker tags will be for Python 3.6 soon:

latest
flask (deprecated)
flask-index (deprecated)
flask-upload (deprecated)
flask-index-upload (deprecated)

Also, the following Docker tags will be deprecated soon,
use the new and improved tags:

flask
flask-index
flask-upload
flask-index-upload
flask-python2.7
flask-python3.5
flask-python3.5-index
flask-python3.5-upload
flask-python3.5-index-upload


If you need Python 2.7, specify it with:

FROM tiangolo/uwsgi-nginx-flask:python2.7

If you need Python 3.6, specify it with:

FROM tiangolo/uwsgi-nginx-flask:python3.6

Find more options in the documentation:

https://github.com/tiangolo/uwsgi-nginx-flask-docker

Listen to the cow..."

for i in {1..6}
do
   cowsay "WARNING: don't use 'latest', instead use:

FROM tiangolo/uwsgi-nginx-flask:python2.7

or

FROM tiangolo/uwsgi-nginx-flask:python3.6";

   sleep 10;
done

exec "$@"
