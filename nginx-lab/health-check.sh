#!/usr/bin/bash

# This script runs a health-check on the nginx lab instance automatically

# tests application availability
echo "Checking app availability..."

http_code=$(curl -s -o /dev/null --noproxy '*' --max-time 5 -w "%{http_code}" http://127.0.0.1:8081)

code=$?

if [[ "$code" -eq 0 && "$http_code" -eq 200 ]]
then
    echo "$(date '+%Y-%m-%d %H:%M:%S') | HEALTHY | HTTP 200" >> "$HOME/cloud-engineering/nginx-lab/logs/health-check.log"
    exit 0
elif [[ "$code" -eq 0 && "$http_code" -eq 404 ]]
then
    echo "$(date '+%Y-%m-%d %H:%M:%S') | UNHEALTHY | HTTP 404" >> "$HOME/cloud-engineering/nginx-lab/logs/health-check.log"
    exit 1
else
    echo "Server returned an error status: $http_code"
    exit 1
fi



