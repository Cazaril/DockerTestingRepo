#!/bin/bash
asadmin start-domain &

sleep 15

python /entrypoint.py
