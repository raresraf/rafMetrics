#!/bin/bash

mkdir -p ./output/
python ./WebMonitoring/WebsiteMonitorHelpers/speedprofile.py -p ./output/ -b chrome -u "$@"
