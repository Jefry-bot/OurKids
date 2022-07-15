#!/bin/bash

echo "Service complaint current in port 4000"
echo ""
source $2-complaint/$1
python3 $2-complaint/src/index.py
deactivate