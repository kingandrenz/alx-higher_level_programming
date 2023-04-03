#!/bin/bash
#send request and display response
curl -sl "$1" | grep -i "Content-Length" | awk '{print $2}'
