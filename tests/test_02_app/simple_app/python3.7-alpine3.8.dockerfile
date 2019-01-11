FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.8

COPY ./app/main.py /app/main.py
COPY ./app/static /app/static
