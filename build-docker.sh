#!/bin/sh

VERSION=$(python scripts/dump-version.py)
WORKDIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

CMD="docker build -t dotbot:latest-dev -t dotbot:${VERSION}-dev ."
echo "$CMD"

eval $CMD
