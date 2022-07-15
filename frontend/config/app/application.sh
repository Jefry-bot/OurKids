#!/bin/bash

source $2-application/$1
python3 $2-application/src/index.py
deactivate