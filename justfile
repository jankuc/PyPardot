#!/usr/bin/env just --justfile

hello:
  echo "hello world"

build:
  source pypardot4_env/bin/activate
  pip install -e .