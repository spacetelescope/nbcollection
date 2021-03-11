#!/usr/bin/env bash

set -e

export LANG=C.UTF-8
export LC_ALL=C.UTF-8

git clone https://github.com/spacetelescope/nbcollection nbcollection
cd nbcollection
git checkout ee085023f565abc0b177932321caf2e3fda5e040
pip install -U pip setuptools
pip install -r ci_requirements.txt
python setup.py install
cd -
