#!/bin/bash

ACTUAL=$(pwd)

if [[ -e "$ACTUAL/python3" ]]
then 
    ROUTE=$ACTUAL/../../service
    PYTHON3=$ACTUAL/python3
else
    ROUTE=$ACTUAL/service
    PYTHON3=$ACTUAL/config/app/python3 
fi

if [[ -e "$ACTUAL/app" ]]
then
    ROUTE=$ACTUAL/../service
    PYTHON3=$ACTUAL/app/python3 
fi

ACTIVATE=env/bin/activate

$PYTHON3 -m venv $ROUTE-show-view/env
source $ROUTE-show-view/$ACTIVATE
pip install -r $ROUTE-show-view/requirements.txt
deactivate

$PYTHON3 -m venv $ROUTE-application/env
source $ROUTE-application/$ACTIVATE
pip install -r $ROUTE-application/requirements.txt
deactivate