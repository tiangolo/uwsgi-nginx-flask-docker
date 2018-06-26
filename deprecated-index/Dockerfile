FROM tiangolo/uwsgi-nginx-flask:python2.7

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN apt-get update && apt-get install -y cowsay

ENV PATH $PATH:/usr/games

# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
ENV STATIC_INDEX 1
# ENV STATIC_INDEX 0

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/bin/supervisord"]