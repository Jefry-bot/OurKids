#!/bin/bash

ACTUAL=$(pwd)

sudo kill -9 `sudo lsof -t -i:4000`
sudo kill -9 `sudo lsof -t -i:4001`

clear

if [[ -e "$ACTUAL/python3" ]]
then 
    ROUTE=$ACTUAL
else
    ROUTE=$ACTUAL/config/app
fi

if [[ -e "$ACTUAL/app" ]]
then
    ROUTE=$ACTUAL/app
fi

ACTIVATE=env/bin/activate
ROUTE_SERVICE=$ROUTE/../../service

. $ROUTE/complaint.sh $ACTIVATE $ROUTE_SERVICE &
. $ROUTE/security.sh $ACTIVATE $ROUTE_SERVICE