#!/bin/bash

cd /home/ubuntu/Smart-Energy-Service/all_things/Smart-Energy-yaml/EdgeX_kubernetes/Edgex-Kubernetes/edgex-on-kubernetes
./hack/edgex-up.sh
cd /home/ubuntu/Smart-Energy-Service/all_things/Smart-Energy-yaml
kubectl apply -f zookeeper.yaml
kubectl apply -f kafka.yaml
kubectl apply -f influx_chro.yaml
kubectl apply -f api_server.yaml
kubectl apply -f consumer_device1.yaml



