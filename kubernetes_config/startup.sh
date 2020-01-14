#!/bin/bash

# Start minikube VM
minikube start

# Enable access to k8s dashboard
kubectl proxy --accept-hosts='.*' --address=192.168.100.187 &

# Remove known_host
ssh-keygen -f "/home/rares/.ssh/known_hosts" -R "192.168.99.105"

# Tunnels
ssh -i ~/.minikube/machines/minikube/id_rsa docker@$(minikube ip) -fN -L \*:31000:0.0.0.0:31000 -oStrictHostKeyChecking=no
ssh -i ~/.minikube/machines/minikube/id_rsa docker@$(minikube ip) -fN -L \*:31001:0.0.0.0:31001 -oStrictHostKeyChecking=no
ssh -i ~/.minikube/machines/minikube/id_rsa docker@$(minikube ip) -fN -L \*:31002:0.0.0.0:31002 -oStrictHostKeyChecking=no