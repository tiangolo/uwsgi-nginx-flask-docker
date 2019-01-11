FROM tiangolo/uwsgi-nginx-flask:python2.7

COPY ./app/main.py /app/main.py
COPY ./app/static /app/static
