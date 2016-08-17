#! /usr/bin/env bash

# Compress all the example directories in .zip files to be uploaded for a release
mkdir ./dist
for f in example-flask* ; do
  if [[ -d $f ]] ; then
    zip -r ./dist/$f.zip $f ;
  fi ;
done;
