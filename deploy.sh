#!/bin/bash

if [ -z "$1" ]
  then
    echo "Usage: ./deploy.sh <metricsui>"
    echo "No argument supplied"
    exit
fi

curr_time=$(date +%Y%m%d%H%M%S)

if [[ $1 == "metricsui" ]]
   then
	npm install
	npm run-script build
        sudo docker build -f Dockerfile -t raresraf/metricsui:$curr_time .
	sudo docker push raresraf/metricsui:$curr_time
	sed "s/raresraf\/metricsui/raresraf\/metricsui:$curr_time/g" deploy/template_metricsui.yaml > deploy/metricsui.yaml
	kubectl apply -f deploy/metricsui.yaml
fi
