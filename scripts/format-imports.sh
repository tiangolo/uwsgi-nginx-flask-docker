#!/usr/bin/env bash
set -x

# Sort imports one per line, so autoflake can remove unused imports
isort --recursive  --force-single-line-imports --apply ./
sh ./scripts/format.sh
