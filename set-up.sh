#!/bin/sh

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

echo "now run: 'source .venv/bin/activate'"
