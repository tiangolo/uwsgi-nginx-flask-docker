FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app/main.py /app/main.py
COPY ./app/static /app/static
