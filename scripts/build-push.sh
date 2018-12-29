#!/usr/bin/env bash

set -e

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

docker-compose -f docker-compose.build.stage01.yml build

docker-compose -f docker-compose.build.stage01.yml push

docker-compose -f docker-compose.build.stage02.yml build

docker-compose -f docker-compose.build.stage02.yml push
