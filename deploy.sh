#!/bin/bash
echo "update"
sudo apt-get update

echo "python 3.10 install"
sudo apt-get install python3.10 -y
echo python --version

echo "pip install"
sudo apt install python3-pip -y
echo pip3 --version

echo "pocketsphinx install"
pip3 install pocketsphinx

echo "server start"
python3 request_handler.py
