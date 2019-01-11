FROM tiangolo/uwsgi-nginx-flask:latest

COPY ./app/main.py /app/main.py
COPY ./app/static /app/static