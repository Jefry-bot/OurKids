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

$PYTHON3 -m venv $ROUTE-complaint/env
source $ROUTE-complaint/$ACTIVATE
pip install -r $ROUTE-complaint/requirements.txt
deactivate

$PYTHON3 -m venv $ROUTE-security/env
source $ROUTE-security/$ACTIVATE
pip install -r $ROUTE-security/requirements.txt
deactivate

$PYTHON3 -m venv $ROUTE-application/env
source $ROUTE-application/$ACTIVATE
pip install -r $ROUTE-application/requirements.txt
deactivate