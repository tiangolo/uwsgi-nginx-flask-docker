FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7

COPY ./app/main.py /app/main.py
COPY ./app/static /app/static
