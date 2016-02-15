FROM tiangolo/uwsgi-nginx:latest

MAINTAINER Sebastian Ramirez <tiangolo@gmail.com>

RUN pip install flask

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copy sample app
COPY ./app /app
