#!/bin/bash

while :
do
	sleep 6h

  # Periodically restart VM
	minikube stop

	# Startup
	./startup.sh
done
