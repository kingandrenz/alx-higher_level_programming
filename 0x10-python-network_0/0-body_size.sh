#!/bin/bash
#send request and display response
curl -sl "$1" | grep -i "Content-Length" | cut -d ' ' -f 2
