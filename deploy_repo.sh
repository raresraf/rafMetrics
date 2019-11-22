#!/bin/bash

# ALL_MODULES : ['login', 'webmonitoringapi', 'resource', 'website']

if [ -z "$1" ]
  then
    echo "Usage: ./deploy_repo.sh <login, webmonitoringapi, resource, website>"
    echo "No argument supplied"
    exit
fi

for var in "$@"
do
  if [[ $var == "login" ]]
   then
    ./Login/deploy.sh login
  fi
  if [[ $var == "webmonitoringapi" ]]
   then
    ./WebMonitoring/API/deploy.sh webmonitoringapi
  fi
  if [[ $var == "resource" ]]
   then
    ./WebMonitoring/deploy.sh resource
  fi
  if [[ $var == "website" ]]
   then
    ./WebMonitoring/deploy.sh website
  fi
done
