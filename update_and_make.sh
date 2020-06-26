#!/bin/bash

git fetch upstream
git merge upstream/master

./make_figures.py

git add --all
git commit -m "updating figures"
git push origin master

