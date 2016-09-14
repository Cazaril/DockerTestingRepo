#!/bin/bash


################################## ENVIRONMENT VARIABLES NEEDED ############################

if [ -z $PAYPAL_CLIENT_ID ];
then
    echo $PAYPAL_CLIENT_ID environment variable not set
    exit 1
fi

if [ -z $PAYPAL_CLIENT_SECRET ];
then
    echo $PAYPAL_CLIENT_SECRET environment variable not set
    exit 1
fi

if [ -z $BIZ_ECOSYS_PORT ];
then
    echo $BIZ_ECOSYS_PORT environment variable not set
    exit 1
fi

if [ -z $BIZ_ECOSYS_HOST ];
then
    echo $BIZ_ECOSYS_HOST environment variable not set
    exit 1
fi

if [[ -z $RSS_CLIENT_ID ]];
then
    echo $RSS_CLIENT_ID is not set
    exit 1
fi

if [[ -z $RSS_SECRET ]];
then
    echo $RSS_SECRET is not set
    exit 1
fi
if [[ -z $RSS_URL ]];
then
    echo $RSS_URL is not set
    exit 1
fi

if [[ -z $OAUTH2_CLIENT_ID ]];
then
    echo $OAUTH2_CLIENT_ID is not set
    exit 1
fi

if [[ -z $OAUTH2_CLIENT_SECRET ]];
then
    echo $OAUTH2_CLIENT_SECRET is not set
    exit 1
fi


############################################################################################


set -o monitor

service mongodb start

/usr/local/bin/docker-entrypoint.sh mysqld "$@" &

asadmin start-domain &

i=1

exec 8<>/dev/tcp/127.0.0.1/3306
mysqlStatus=$?
doneTables=1
exec 9<>/dev/tcp/127.0.0.1/4848
glassfishStatus=$?
doneGlassfish=1
exec 10<>/dev/tcp/127.0.0.1/28017
mongodbStatus=$?
doneMongo=1

while [[ $mysqlStatus -ne 0 || $glassfishStatus -ne 0 || $mongodbStatus -ne 0 && $i -lt 20 ]]; do
    sleep 2
    i=$i+1
    
    if [[ $mysqlStatus -eq 0 && $doneTables -eq 1 ]];
    then
	create_tables
	doneTables=0
    elif [[ $mysqlStatus -ne 0 ]];
    then
	exec 8<>/dev/tcp/127.0.0.1/3306
	mysqlStatus=$?
    fi

    if [[ $glassfishStatus -eq 0 && $doneGlassfish -eq 1 ]];
    then
	glassfish_related
	doneGlassfish=0
    elif [[ $glassfishStatus -ne 0]];
    then
	exec 9<>/dev/tcp/127.0.0.1/4848
	glassfishStatus=$?
    fi

    if [[ $mongodbStatus -eq 0 && $doneMongo -eq 1 ]];
    then
	# TODO
	doneMongo=0
    elif [[ $mongodbStatus -ne 0 ]];
    then
	exec 10<>/dev/tcp/127.0.0.1/28017
	mongodbStatus=$?
    fi
done

if [[ $i -eq 20 ]];
then
    echo Conection to Mongo returned $mongoStatus
    echo Conection to MySQL returned $mysqlStatus
    echo Conection to Glassfish returned $glassfishStatus
    exit 1
fi

exec 8>&- # close output connection
exec 8<&- # close input connection
exec 9>&- # close output connection
exec 9<&- # close input connection
exec 10>&- # close output connection
exec 10<&- # close input connection

function create_tables {
    mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSPRODUCTCATALOG2;"

    mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSPRODUCTORDERING;"

    mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSPRODUCTINVENTORY;"

    mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSPARTYMANAGEMENT;"

    mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSBILLINGMANAGEMENT;"

    mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSCUSTOMER;"

    mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS DSUSAGEMANAGEMENT;"

    mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS RSS;"
}

function glassfish_related {
    python /entrypoint.py
}

/business-ecosystem-logic-proxy/node-v4.5.0-linux-x64/bin/node server.js &

fg 1
