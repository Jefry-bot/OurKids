#!/bin/bash

sleep 2
echo ""
echo "Service security current in port 4001"
echo ""

source $2-security/$1
python3 $2-security/src/index.py
deactivate