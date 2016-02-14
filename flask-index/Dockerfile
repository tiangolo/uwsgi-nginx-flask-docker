FROM tiangolo/uwsgi-nginx:flask

MAINTAINER Sebastian Ramirez <tiangolo@gmail.com>

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copy sample app
COPY ./app /app
