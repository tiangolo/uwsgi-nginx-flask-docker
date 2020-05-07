#!/usr/bin/env bash
set -e

bash scripts/build.sh
pytest tests
