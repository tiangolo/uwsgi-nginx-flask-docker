#!/usr/bin/env bash
set -e

use_tag="tiangolo/uwsgi-nginx-flask:$NAME"

DOCKERFILE="$NAME"

if [ "$NAME" == "latest" ] ; then
    DOCKERFILE="python3.7"
fi

docker build -t "$use_tag" --file "./docker-images/${DOCKERFILE}.dockerfile" "./docker-images/"
