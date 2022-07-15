#!/bin/bash

sleep 1

source $2-application/$1
python3 $2-application/src/index.py
deactivate