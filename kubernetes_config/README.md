# Kubernetes Config

Keeps track of all k8s settings

# Quick deploy in minikube

```
./startup.sh
```

# Fault-tolerant minikube deploy

Periodic restarts - 6 hours

```
./run.sh
```

## Deployments

- `mysql` : An open-source relational database management system 📙
- `resourcemonitor` : Manage and monitor resources, recording crawled data in DB 🐦
- `websitemonitor` : Manage and monitor websites, recording crawled data in DB 🐦
- `login-deployment` : Ensure smooth login procedure 🔒
- `webmonitoringapi-deployment` : Expose an API for WebMonitoring Tool 🛠️
- `metricsui` : FE deploy for rafMetrics project - Powered by React ❤️

## Services

### NodePort Allocation

The default node port range for Kubernetes is 30000 - 32767.

The following ports are currently in use:

- `31000` - metricsui
- `31001` - login
- `31002` - webmonitoringapi

### ClusterIPs Allocated

The following Cluster IPs are currently in use:

- `10.96.0.1` - kubernetes
- `10.96.0.2` - mysql
- `10.96.0.3` - login
- `10.96.0.4` - webmonitoringapi
