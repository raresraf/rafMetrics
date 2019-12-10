# rafMetrics
Metrics for evaluating the performance and complexity of computer programs


## Components:
### WebMonitoring
A tool for monitoring multiple network resources and websites. 
Gather data by periodically monitoring specific resources and websites and stores results in database.

#### ResourceManager
Monitors all resources by periodically (timer set default at 1 hour interval) sending requests to existing resources.
Store simple metrics like total time or total requests answer as entries in DB. 

#### WebsiteManager
Monitors all websites by periodically (timer set default at 1 hour interval) generating a HAR (HTTP-Archieve data performance file) for loading metrics corresponding to a website, with Chrome using Browsermob-Proxy.
Also parse and store valuable insights resulted from the HAR file into DB.

#### WebMonitoring API
Provide an API for interrogating useful metrics from DB.

### Login
Backend implementation to provide a simple authentication, registration and management for users inside rafMetrics platform.

### KubernetesConfig
Keeps track of all k8s settings

### MySQL
Database used to store persistent data required by Login and WebMonitoring.
All relations are kept in **Boyce-Codd Normal Form**.

### deploy_repo.sh
Simple script to ensure dockerize and deployment in Kubernetes for all backend components

### metricsUI
Frontend implementation of rafMetrics platform based on Flatboard template


## Class Diagram
![alt text]("https://github.com/raresraf/rafMetrics/raw/master/classes.png")

## Packages Diagram
![alt text]("https://github.com/raresraf/rafMetrics/raw/master/packages.png")
