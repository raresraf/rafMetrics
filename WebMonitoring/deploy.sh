#!/bin/bash

if [ -z "$1" ]
  then
    echo "Usage: ./deploy.sh <resource | website>"
    echo "No argument supplied"
    exit
fi

curr_time=$(date +%Y%m%d%H%M%S)

if [[ $1 == "resource" ]]
   then
	sudo docker build -f DockerfileResource -t raresraf/resourcemonitor:$curr_time ../
	sudo docker push raresraf/resourcemonitor:$curr_time
	sed "s/raresraf\/resourcemonitor/raresraf\/resourcemonitor:$curr_time/g" deploy/template_deployment_resource.yaml > deploy/deployment_resource.yaml
	kubectl apply -f deploy/deployment_resource.yaml
fi

	
if [[ $1 == "website" ]]
then
	sudo docker build -f DockerfileWebsite -t raresraf/websitemonitor:$curr_time ../
	sudo docker push raresraf/websitemonitor:$curr_time
	sed "s/raresraf\/websitemonitor/raresraf\/websitemonitor:$curr_time/g" deploy/template_deployment_website.yaml > deploy/deployment_website.yaml
	kubectl apply -f deploy/deployment_website.yaml
fi
