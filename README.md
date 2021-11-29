# rafMetrics


**Now published**: [A new metric for evaluating the performance and complexity of computer programs: A new approach to the traditional ways of measuring the complexity of algorithms and estimating running times](https://ieeexplore.ieee.org/abstract/document/9481065) at the 2021 23rd International Conference on Control Systems and Computer Science (CSCS).

```
@INPROCEEDINGS{9481065,
  author={Folea, Rares and Slusanschi, Emil-Ioan},
  booktitle={2021 23rd International Conference on Control Systems and Computer Science (CSCS)}, 
  title={A new metric for evaluating the performance and complexity of computer programs: A new approach to the traditional ways of measuring the complexity of algorithms and estimating running times}, 
  year={2021},
  volume={},
  number={},
  pages={157-164},
  abstract={This paper presents a refined complexity calculus model: r-Complexity, a new asymptotic notation that offers better complexity feedback for similar programs than the traditional Bachmann-Landau notation, providing subtle insights even for algorithms that are part of the same conventional complexity class. The architecture-dependent metric represents an enhancement that provides better sensitivity with respect to discrete analysis.},
  keywords={},
  doi={10.1109/CSCS52396.2021.00033},
  ISSN={2379-0482},
  month={May},}
```

---

![Python application](https://github.com/raresraf/rafMetrics/workflows/Python%20application/badge.svg)
![Codecov](https://github.com/raresraf/rafMetrics/workflows/Codecov/badge.svg)
![Code scanning - action](https://github.com/raresraf/rafMetrics/workflows/Code%20scanning%20-%20action/badge.svg)


[![CodeFactor](https://www.codefactor.io/repository/github/raresraf/rafmetrics/badge)](https://www.codefactor.io/repository/github/raresraf/rafmetrics)
[![codecov](https://codecov.io/gh/raresraf/rafMetrics/branch/master/graph/badge.svg)](https://codecov.io/gh/raresraf/rafMetrics)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/raresraf/rafMetrics/?ref=repository-badge)

Metrics for evaluating the performance and complexity of computer programs.


- Written Material: [here](TeX/diploma-proiect-template.pdf)
- Presentation: [here](docs/SCS2020/SCS2020RaresFoleaPresentation.pdf)
- Short Material: [here](docs/SCS2020/SCS2020RaresFoleaMaterial.pdf)

Part of Bachelor Thesis @ CS
- Full Material: [here](docs/LICENTA2020/Licenta2020-Rares_Folea.pdf)
- Presentation (ro): [here](docs/LICENTA2020/proiect_licenta_acs_Folea_O_Rares_98884.pdf)
- Short demo: [link](https://www.youtube.com/watch?v=2XpVoseXwvo)


![rafMetrics](docs/logo.jpg?raw=true "rComplexity")


## Components:

### rafComputing

The ML-based tool implementing the process of automatically tailoring a suitable rComplexity Class for an algorithm.

![rafMetrics](docs/bigtheta.png?raw=true "rComplexity")

NOTE: Improved version: https://github.com/raresraf/rafPipeline/tree/master/rComplexity

### WebMonitoring

A tool for monitoring multiple network resources and websites.
Gather data by periodically monitoring specific resources and websites and stores results in database.

#### ResourceManager

Monitors all resources by periodically (timer set default at 1 hour interval) sending requests to existing resources.
Store simple metrics like total time or total requests answer as entries in DB.

#### WebsiteManager

Monitors all websites by periodically (timer set default at 1 hour interval) generating a HAR (HTTP-Archieve data performance file) for loading metrics corresponding to a website, with Chrome using Browsermob-Proxy.
Also parse and store valuable insights resulted from the HAR file into DB.
The service uses [speedprofile](https://github.com/parasdahal/speedprofile) engine.

#### WebMonitoring API

Provide an API for interrogating useful metrics from DB.

### Login

Backend implementation to provide a simple authentication, registration and management for users inside rafMetrics platform.

### DockerConfig

Keeps track of all Docker Compose/Docker Swarm settings and configurations.

### KubernetesConfig

Keeps track of all k8s settings

### MySQL

Database used to store persistent data required by Login and WebMonitoring.
All relations are kept in **Boyce-Codd Normal Form**.

### deploy_repo.sh

Simple script to ensure dockerize and deployment in Kubernetes for all backend components

### metricsUI

Frontend implementation of rafMetrics platform based on Flatlogic Template: React Material Admin — Material-UI Dashboard
