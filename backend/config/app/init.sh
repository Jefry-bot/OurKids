#!/bin/bash

ACTUAL=$(pwd)

sudo kill -9 `sudo lsof -t -i:4000`
sudo kill -9 `sudo lsof -t -i:4001`

clear

if [[ -e "$ACTUAL/python3" ]]
then 
    ROUTE=$ACTUAL
    PYTHON3=$ACTUAL/python3
else
    ROUTE=$ACTUAL/config/app
    PYTHON3=$ACTUAL/config/app/python3
fi

if [[ -e "$ACTUAL/app" ]]
then
    ROUTE=$ACTUAL/app
    PYTHON3=$ACTUAL/app/python3
fi

ACTIVATE=env/bin/activate
ROUTE_SERVICE=$ROUTE/../../service

. $ROUTE/complaint.sh $ACTIVATE $PYTHON3 $ROUTE_SERVICE & 
. $ROUTE/security.sh $ACTIVATE $PYTHON3 $ROUTE_SERVICE