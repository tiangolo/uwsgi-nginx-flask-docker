FROM tiangolo/uwsgi-nginx-flask:python2.7-alpine3.8

COPY ./app/main.py /app/main.py
COPY ./app/static /app/static
