FROM tiangolo/uwsgi-nginx-flask:python3.5

COPY ./app/main.py /app/main.py
COPY ./app/static /app/static
