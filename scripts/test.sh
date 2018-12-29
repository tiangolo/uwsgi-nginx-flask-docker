#!/usr/bin/env bash
set -e

docker-compose -f docker-compose.build.stage01.yml build
