# Kubernetes Config
Keeps track of all k8s settings


## Deployments

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

