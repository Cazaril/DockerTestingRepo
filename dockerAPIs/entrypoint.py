#!/usr/bin/env python
# Credits of this code to @Rock_Neurotiko
from sh import asadmin, cd
import sys

DBUSER = "root"
DBPWD = "toor"
DBHOST = "localhost"
DBPORT = 3306

APIS = [{"url": "https://github.com/FIWARE-TMForum/DSPRODUCTCATALOG2.git",
         "bbdd": "DSPRODUCTCATALOG2",
         "war": "target/DSPRODUCTCATALOG2.war",
         "root": "DSProductCatalog",
         "name": "catalog",
         "resourcename": "jdbc/pcatv2"},
        {"url": "https://github.com/FIWARE-TMForum/DSPRODUCTORDERING.git",
         "bbdd": "DSPRODUCTORDERING",
         "war": "target/productOrdering.war",
         "root": "DSProductOrdering",
         "name": "ordering",
         "resourcename": "jdbc/podbv2"},
        {"url": "https://github.com/FIWARE-TMForum/DSPRODUCTINVENTORY.git",
         "bbdd": "DSPRODUCTINVENTORY",
         "war": "target/productInventory.war",
         "root": "DSProductInventory",
         "name": "inventory",
         "resourcename": "jdbc/pidbv2"},
        {"url": "https://github.com/FIWARE-TMForum/DSPARTYMANAGEMENT.git",
         "bbdd": "DSPARTYMANAGEMENT",
         "war": "target/party.war",
         "root": "DSPartyManagement",
         "name": "party",
         "resourcename": "jdbc/partydb"},
        {"url": "https://github.com/FIWARE-TMForum/DSBILLINGMANAGEMENT.git",
         "bbdd": "DSBILLINGMANAGEMENT",
         "war": "target/billingManagement.war",
         "root": "DSBillingManagement",
         "name": "billing",
         "resourcename": "jdbc/bmdbv2"},
        {"url": "https://github.com/FIWARE-TMForum/DSCUSTOMER.git",
         "bbdd": "DSCUSTOMER",
         "war": "target/customer.war",
         "root": "DSCustomerManagement",
         "name": "customer",
         "resourcename": "jdbc/customerdbv2"},
        {"url": "https://github.com/FIWARE-TMForum/DSUSAGEMANAGEMENT.git",
         "bbdd": "DSUSAGEMANAGEMENT",
         "war": "target/usageManagement.war",
         "root": "DSUsageManagement",
         "name": "usage",
         "resourcename": "jdbc/usagedbv2"}]

rss = {"url": "https://github.com/FIWARE-TMForum/business-ecosystem-rss.git",
       "branch": "develop",
       "bbdd": "RSS",
       "war": "fiware-rss/target/DSRevenueSharing.war",
       "name": "rss",
       "root": "DSRevenueSharing"}

# asadmin create-jdbc-connection-pool --restype java.sql.Driver --driverclassname com.mysql.jdbc.Driver --property 'user=<user>:password=<pwd>:URL="<url>"' <name>
def pool(name, user, pwd, url):
    asadmin("create-jdbc-connection-pool",
            "--restype",
            "java.sql.Driver",
            "--driverclassname",
            "com.mysql.jdbc.Driver",
            "--property",
            "user={}:password={}:URL={}".format(user, pwd, url.replace(":", "\:")),
            name)

# asadmin create-jdbc-resource --connectionpoolid <poolname> <jndiname>
def resource(name, pool):
    asadmin("create-jdbc-resource", "--connectionpoolid", pool, name)

def generate_mysql_url(db):
    return "jdbc:mysql://{}:{}/{}".format(DBHOST, DBPORT, db)

if "install" in sys.argv:
    for api in APIS:
        pool(api.get("bbdd"), DBUSER, DBPWD, generate_mysql_url(api.get("bbdd")))
        url = api.get("url")
        pool = url.split("/")[-1][:-4]
        resource(api.get("resourcename"), pool)

    for api in APIS + [rss]:
        cd(wars)
        asadmin("deploy", "--force", "true" if force else "false", "--contextroot", api.get('root'), "--name", api.get('root'), api.get('war'))
else:
    asadmin("start-domain")