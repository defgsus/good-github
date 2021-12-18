#!/bin/bash

cd ../frontend || exit
rm -r dist/*
yarn build || exit

rm ../docs/index*.*
rm ../docs/js/*.*
cp dist/index.html ../docs/
cp dist/index*.js ../docs/js/
cp dist/index*.css ../docs/js/
