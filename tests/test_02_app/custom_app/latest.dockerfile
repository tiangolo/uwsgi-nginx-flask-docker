FROM tiangolo/uwsgi-nginx-flask:latest

COPY ./application /application
COPY ./prestart.sh /app/prestart.sh
WORKDIR /application

EXPOSE 8080
