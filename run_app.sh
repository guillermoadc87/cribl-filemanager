#!/bin/bash 

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

PORTS="${FLASK_PORT:-5000}"

echo "Starting Server"
gunicorn wsgi --preload --certfile=cert/demo.crt --keyfile=cert/demo.key --timeout 900 -w 2 -b 0.0.0.0:$PORTS