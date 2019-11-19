#!/bin/bash

if [ -z "$1" ]
  then
    echo "Usage: ./deploy.sh <webmonitoringapi>"
    echo "No argument supplied"
    exit
fi

curr_time=$(date +%Y%m%d%H%M%S)

if [[ $1 == "webmonitoringapi" ]]
   then
	sudo docker build -f Dockerfile -t raresraf/webmonitoringapi:$curr_time ../../
	sudo docker push raresraf/webmonitoringapi:$curr_time
	sed "s/raresraf\/webmonitoringapi/raresraf\/webmonitoringapi:$curr_time/g" deploy/template_webmonitoringapi.yaml > deploy/webmonitoringapi.yaml
	kubectl apply -f deploy/webmonitoringapi.yaml
fi
