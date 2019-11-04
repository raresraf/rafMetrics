#!/bin/bash

mkdir -p output/
python ./WebsiteMonitorHelpers/speedprofile.py -p output/ -b chrome -u "$@"
