#!/bin/bash

if [ -z "$1" ]
  then
    echo "Usage: ./deploy.sh <login>"
    echo "No argument supplied"
    exit
fi

curr_time=$(date +%Y%m%d%H%M%S)

if [[ $1 == "login" ]]
   then
	sudo docker build -f Dockerfile -t raresraf/login:$curr_time ../
	sudo docker push raresraf/login:$curr_time
	sed "s/raresraf\/login/raresraf\/login:$curr_time/g" deploy/template_login.yaml > deploy/login.yaml
	kubectl apply -f deploy/login.yaml
fi
