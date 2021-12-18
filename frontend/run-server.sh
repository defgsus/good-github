#!/bin/bash

function run_data_server() {
  cd ../docs/ || exit
  python -m http.server 8008 || exit
}

function run_web_server() {
  rm -r dist/*
  yarn start || exit
}

run_data_server & run_web_server

wait
