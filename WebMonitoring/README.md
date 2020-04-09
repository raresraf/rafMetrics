# WebMonitoring

A tool for monitoring multiple network resources and websites.

Implementation hierarchy of WebMonitoring Project:

## API

Described in WebMonitoring API definition

## Dockerfile

There are provided two different Dockerfiles for ResourceMonitoring and WebsiteMonitoring services

```
.
├── DockerfileResource
├── DockerfileWebsite
```

## Managers

Wrappers over actual engines for monitoring resources and websites, including a speedprofile client implementation.

```
.
├── ResourceManager.py
├── WebsiteManager.py
├── WebsiteMonitorHelpers
│   ├── README.md
│   ├── entrypoint.sh
│   ├── request_helpers.py
│   └── speedprofile.py
├── clients
│   ├── SpeedprofileClient.py
├── configs
│   ├── __init__.py
│   ├── constants.py
│   └── settings.py
└── monitors
    ├── ResourceMonitor.py
    ├── WebsiteMonitor.py
    └── __init__.py
```
