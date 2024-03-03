#!/bin/bash

sudo pip3 uninstall pocketsphinx -y
echo "pocketsphinx removed"

sudo apt-get remove python3-pip -y
echo "pip removed"
