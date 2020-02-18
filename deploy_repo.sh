#!/bin/bash

ALL_MODULES=('login' 'webmonitoringapi' 'resource' 'website' 'metricsui')

main() {
  if [ -z "$1" ]; then
    echo "No argument supplied"
    echo ""
    echo "Usage: ./deploy_repo.sh <${ALL_MODULES[*]}>"
    echo ""
    echo "-- You can use one or more options"
    echo "-- If you want to deploy all modules, use: ./deploy_repo.sh ALL"
    exit
  fi

  deploy_modules=("${@}")

  # Check for all|ALL option
  for module in "${deploy_modules[@]}"; do
    if [[ $module == 'all' || $module == 'ALL' ]]; then
      deploy_modules=("${ALL_MODULES[@]}")
    fi
  done

  echo "Deploy procedure started!"
  echo "The following modules will be deployed: <${deploy_modules[*]}>"

  # Current time format: YYYYMMDDHHMMSS
  # e.g. 20191122175120
  curr_time=$(date +%Y%m%d%H%M%S)

  for module in "${deploy_modules[@]}"; do
    # Login deployment
    if [[ $module == "login" ]]; then
      sudo docker build -f Login/Dockerfile -t raresraf/login:$curr_time .
      sudo docker push raresraf/login:$curr_time
      sed "s/raresraf\/login/raresraf\/login:$curr_time/g" kubernetes_config/templates/template_login.yaml > kubernetes_config/latest/login.yaml
      kubectl apply -f kubernetes_config/latest/login.yaml
    fi

    # WebMonitoring API deployment
    if [[ $module == "webmonitoringapi" ]]; then
      sudo docker build -f WebMonitoring/API/Dockerfile -t raresraf/webmonitoringapi:$curr_time .
      sudo docker push raresraf/webmonitoringapi:$curr_time
      sed "s/raresraf\/webmonitoringapi/raresraf\/webmonitoringapi:$curr_time/g" kubernetes_config/templates/template_webmonitoringapi.yaml > kubernetes_config/latest/webmonitoringapi.yaml
      kubectl apply -f kubernetes_config/latest/webmonitoringapi.yaml
    fi

    # ResourceManager deployment
    if [[ $module == "resource" ]]; then
      sudo docker build -f WebMonitoring/DockerfileResource -t raresraf/resourcemonitor:$curr_time .
      sudo docker push raresraf/resourcemonitor:$curr_time
      sed "s/raresraf\/resourcemonitor/raresraf\/resourcemonitor:$curr_time/g" kubernetes_config/templates/template_deployment_resource.yaml > kubernetes_config/latest/deployment_resource.yaml
      kubectl apply -f kubernetes_config/latest/deployment_resource.yaml
    fi

    # WebsiteManager deployment
    if [[ $module == "website" ]]; then
      sudo docker build -f WebMonitoring/DockerfileWebsite -t raresraf/websitemonitor:$curr_time .
      sudo docker push raresraf/websitemonitor:$curr_time
      sed "s/raresraf\/websitemonitor/raresraf\/websitemonitor:$curr_time/g" kubernetes_config/templates/template_deployment_website.yaml > kubernetes_config/latest/deployment_website.yaml
      kubectl apply -f kubernetes_config/latest/deployment_website.yaml
    fi

    # MetricsUI deployment
    if [[ $module == "metricsui" ]]; then
      deploy_metricsui
    fi

  done
}


deploy_metricsui() {
  # React App
  npm install --prefix metricsUI/ metricsUI/
  npm run-script --prefix metricsUI/ build
  sudo docker build -f metricsUI/Dockerfile -t raresraf/metricsui:$curr_time metricsUI/
  sudo docker push raresraf/metricsui:$curr_time
  sed "s/raresraf\/metricsui/raresraf\/metricsui:$curr_time/g" kubernetes_config/templates/template_metricsui.yaml >kubernetes_config/templates/metricsui.yaml
  kubectl apply -f kubernetes_config/templates/metricsui.yaml
}


main "$@"; exit