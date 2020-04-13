#! /bin/bash

source ./venv/bin/activate
gunicorn -w 2 -b 127.0.0.1:5002 main:app
