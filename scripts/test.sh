#!/usr/bin/env bash
set -e

bash scripts/build.sh
SLEEP_TIME=5 pytest tests
