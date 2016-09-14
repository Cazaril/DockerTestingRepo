#!/usr/bin/env bash

asadmin start-domain &
i=1

exec 8<>/dev/tcp/127.0.0.1/4848

while [[ $? -ne 0 && $i -lt 20 ]]; do
    sleep 0.5
    i=$i+1
    exec 8<>/dev/tcp/127.0.0.1/4848
done

exec 9>&- # close output connection
exec 9<&- # close input connection

python /entrypoint.py
