#!/bin/bash

echo $"\napt-get update"
sudo apt-get update &> /dev/null

echo $"\ncheck python version"
sudo python3 --version 2> /dev/null

echo $"\npip install"
sudo apt-get install python3-pip -y &> /dev/null
sudo pip3 --version 2> /dev/null

echo $"\npip update"
sudo pip3 install --upgrade pip -y &> /dev/null
sudo pip3 --version 2> /dev/null

echo $"\npocketsphinx install"
sudo pip3 install pocketsphinx &> /dev/null
sudo pip3 show pocketsphinx 2> /dev/null

echo $"\nserver start"
sudo python3 request_handler.py
