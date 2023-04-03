#!/bin/bash
#send request and display response
curl -sl "$1" | grep "Content-Length" | cut -d  ' ' -f 2
