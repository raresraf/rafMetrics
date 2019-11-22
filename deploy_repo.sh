#!/bin/bash

# ALL_MODULES : ['login', 'webmonitoringapi', 'resource', 'website']

if [ -z "$1" ]
  then
    echo "Usage: ./deploy_repo.sh <login, webmonitoringapi, resource, website>"
    echo "No argument supplied"
    exit
fi

curr_time=$(date +%Y%m%d%H%M%S)

for var in "$@"
do
  if [[ $var == "login" ]]
   then
  sudo docker build -f Dockerfile -t raresraf/login:$curr_time .
    sudo docker push raresraf/login:$curr_time
    sed "s/raresraf\/login/raresraf\/login:$curr_time/g" deploy/template_login.yaml > deploy/login.yaml
    kubectl apply -f deploy/login.yaml
  fi
  if [[ $var == "webmonitoringapi" ]]
  then
    sudo docker build -f Dockerfile -t raresraf/webmonitoringapi:$curr_time .
    sudo docker push raresraf/webmonitoringapi:$curr_time
    sed "s/raresraf\/webmonitoringapi/raresraf\/webmonitoringapi:$curr_time/g" deploy/template_webmonitoringapi.yaml > deploy/webmonitoringapi.yaml
    kubectl apply -f deploy/webmonitoringapi.yaml
  fi
  if [[ $var == "resource" ]]
  then
    sudo docker build -f DockerfileResource -t raresraf/resourcemonitor:$curr_time .
    sudo docker push raresraf/resourcemonitor:$curr_time
    sed "s/raresraf\/resourcemonitor/raresraf\/resourcemonitor:$curr_time/g" deploy/template_deployment_resource.yaml > deploy/deployment_resource.yaml
    kubectl apply -f deploy/deployment_resource.yaml
  fi
  if [[ $var == "website" ]]
  then
    sudo docker build -f DockerfileWebsite -t raresraf/websitemonitor:$curr_time .
    sudo docker push raresraf/websitemonitor:$curr_time
    sed "s/raresraf\/websitemonitor/raresraf\/websitemonitor:$curr_time/g" deploy/template_deployment_website.yaml > deploy/deployment_website.yaml
	  kubectl apply -f deploy/deployment_website.yaml
  fi
done
