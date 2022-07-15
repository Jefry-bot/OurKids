#!/bin/bash

ACTUAL=$(pwd)

sudo kill -9 `sudo lsof -t -i:3000`

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

. $ROUTE/show-view.sh $ACTIVATE $ROUTE_SERVICE &
. $ROUTE/application.sh $ACTIVATE $ROUTE_SERVICE