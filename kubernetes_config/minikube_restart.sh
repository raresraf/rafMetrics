#!/bin/bash

while :
do
	# Startup
	./startup.sh

	sleep 6h

	# Periodically restart VM
	minikube stop
done
