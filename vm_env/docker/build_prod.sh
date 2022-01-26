#!/bin/bash
version=$(awk '/version_api/{print $NF}' version.json | sed 's/,//g' | sed 's/"//g')
echo $version
docker build  -t automation-dev-env . 
docker tag automation-dev-env ghcr.io/extremenetworks/extreme_automation_framework/automation-dev-env:latest
docker tag automation-dev-env ghcr.io/extremenetworks/extreme_automation_framework/automation-dev-env:$version
echo $GIT_PAT | docker login ghcr.io --username=$GIT_USER  --password-stdin
docker push ghcr.io/extremenetworks/extreme_automation_framework/automation-dev-env:latest
docker push ghcr.io/extremenetworks/extreme_automation_framework/automation-dev-env:$version
