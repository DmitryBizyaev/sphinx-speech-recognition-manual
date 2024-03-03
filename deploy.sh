#!/bin/bash

echo "update"
sudo apt-get update &> /dev/null

echo "check python version"
sudo python3 --version 2> /dev/null

echo "pip install"
sudo apt-get install python3-pip -y &> /dev/null
sudo pip3 --version 2> /dev/null

echo "pip update"
sudo pip3 install --upgrade pip -y &> /dev/null
sudo pip3 --version 2> /dev/null

echo "pocketsphinx install"
sudo pip3 install pocketsphinx &> /dev/null
sudo pip3 show pocketsphinx 2> /dev/null

echo "server start"
sudo python3 request_handler.py
