#!/usr/bin/env bash
curl -XPUT http://elasticsearch:9200/$INDEX_NAME -H 'Content-Type: application/json' -d @/opt/wiating/devops/docker_elasticsearch/files/mapping.json