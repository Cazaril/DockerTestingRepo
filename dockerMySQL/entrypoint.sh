#!/bin/bash 

set -o monitor

/usr/local/bin/docker-entrypoint.sh mysqld "$@" &

i=1

exec 8<>/dev/tcp/127.0.0.1/3306

while [[ $? -ne 0 && $i -lt 20 ]]; do
    sleep 2
    i=$i+1
    exec 8<>/dev/tcp/127.0.0.1/3306
done

exec 8>&- # close output connection
exec 8<&- # close input connection

mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSPRODUCTCATALOG2;"

mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSPRODUCTORDERING;"

mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSPRODUCTINVENTORY;"

mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSPARTYMANAGEMENT;"

mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSBILLINGMANAGEMENT;"

mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSCUSTOMER;"

mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSUSAGEMANAGEMENT;"

mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS RSS;"

fg 1
