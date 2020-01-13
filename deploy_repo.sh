#!/bin/bash

# ALL_MODULES : ['login', 'webmonitoringapi', 'resource', 'website', 'metricsui']

if [ -z "$1" ]
  then
    echo "Usage: ./deploy_repo.sh <login, webmonitoringapi, resource, website, metricsui>"
    echo "No argument supplied"
    exit
fi

curr_time=$(date +%Y%m%d%H%M%S)

for var in "$@"
do
  # Login deploy
  if [[ $var == "login" ]]
   then
    sudo docker build -f Login/Dockerfile -t raresraf/login:$curr_time .
    sudo docker push raresraf/login:$curr_time
    sed "s/raresraf\/login/raresraf\/login:$curr_time/g" kubernetes_config/templates/template_login.yaml > kubernetes_config/latest/login.yaml
    kubectl apply -f kubernetes_config/latest/login.yaml
  fi

  # WebMonitoring API deploy
  if [[ $var == "webmonitoringapi" ]]
  then
    sudo docker build -f WebMonitoring/API/Dockerfile -t raresraf/webmonitoringapi:$curr_time .
    sudo docker push raresraf/webmonitoringapi:$curr_time
    sed "s/raresraf\/webmonitoringapi/raresraf\/webmonitoringapi:$curr_time/g" kubernetes_config/templates/template_webmonitoringapi.yaml > kubernetes_config/latest/webmonitoringapi.yaml
    kubectl apply -f kubernetes_config/latest/webmonitoringapi.yaml
  fi

  # ResourceManager deploy
  if [[ $var == "resource" ]]
  then
    sudo docker build -f WebMonitoring/DockerfileResource -t raresraf/resourcemonitor:$curr_time .
    sudo docker push raresraf/resourcemonitor:$curr_time
    sed "s/raresraf\/resourcemonitor/raresraf\/resourcemonitor:$curr_time/g" kubernetes_config/templates/template_deployment_resource.yaml > kubernetes_config/latest/deployment_resource.yaml
    kubectl apply -f kubernetes_config/latest/deployment_resource.yaml
  fi

  # WebsiteManager deploy
  if [[ $var == "website" ]]
  then
    sudo docker build -f WebMonitoring/DockerfileWebsite -t raresraf/websitemonitor:$curr_time .
    sudo docker push raresraf/websitemonitor:$curr_time
    sed "s/raresraf\/websitemonitor/raresraf\/websitemonitor:$curr_time/g" kubernetes_config/templates/template_deployment_website.yaml > kubernetes_config/latest/deployment_website.yaml
	  kubectl apply -f kubernetes_config/latest/deployment_website.yaml
  fi

  # MetricsUI deploy
  if [[ $var == "metricsui" ]]
  then
    npm install metricsUI/
    npm run-script --prefix metricsUI/ build
    sudo docker build -f metricsUI/Dockerfile -t raresraf/metricsui:$curr_time metricsUI/
    sudo docker push raresraf/metricsui:$curr_time
    sed "s/raresraf\/metricsui/raresraf\/metricsui:$curr_time/g" kubernetes_config/templates/template_metricsui.yaml > kubernetes_config/templates/metricsui.yaml
    kubectl apply -f kubernetes_config/templates/metricsui.yaml
  fi


done
