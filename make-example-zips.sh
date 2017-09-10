#! /usr/bin/env bash

# Remove un-needed files
rm -rf ./**/__pycache__

# Compress all the example directories in .zip files to be uploaded for a release
rm -rf ./dist
mkdir ./dist
for f in example-flask* ; do
  if [[ -d $f ]] ; then
    zip -r ./dist/$f.zip $f ;
  fi ;
done;
