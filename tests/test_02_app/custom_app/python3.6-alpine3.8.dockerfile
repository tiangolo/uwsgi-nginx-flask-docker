FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8

COPY ./application /application
COPY ./prestart.sh /app/prestart.sh
WORKDIR /application

EXPOSE 8080
