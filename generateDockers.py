import re

DBUSER = "root"
DBPWD = "toor"
DBHOST = "localhost"
DBPORT = 3306

APIS = [
    {"url": "https://github.com/FIWARE-TMForum/DSPRODUCTCATALOG2.git",
     "branch": "master",
     "bbdd": "DSPRODUCTCATALOG2",
     "war": "target/DSPRODUCTCATALOG2.war",
     "root": "DSProductCatalog",
     "name": "catalog",
     "resourcename": "jdbc/pcatv2"},
    {"url": "https://github.com/FIWARE-TMForum/DSPRODUCTORDERING.git",
     "branch": "develop",
     "bbdd": "DSPRODUCTORDERING",
     "war": "target/productOrdering.war",
     "root": "DSProductOrdering",
     "name": "ordering",
     "resourcename": "jdbc/podbv2"},
    {"url": "https://github.com/FIWARE-TMForum/DSPRODUCTINVENTORY.git",
     "branch": "develop",
     "bbdd": "DSPRODUCTINVENTORY",
     "war": "target/productInventory.war",
     "root": "DSProductInventory",
     "name": "inventory",
     "resourcename": "jdbc/pidbv2"},
    {"url": "https://github.com/FIWARE-TMForum/DSPARTYMANAGEMENT.git",
     "branch": "develop",
     "bbdd": "DSPARTYMANAGEMENT",
     "war": "target/party.war",
     "root": "DSPartyManagement",
     "name": "party",
     "resourcename": "jdbc/partydb"},
    {"url": "https://github.com/FIWARE-TMForum/DSBILLINGMANAGEMENT.git",
     "branch": "develop",
     "bbdd": "DSBILLINGMANAGEMENT",
     "war": "target/billingManagement.war",
     "root": "DSBillingManagement",
     "name": "billing",
     "resourcename": "jdbc/bmdbv2"},
    {"url": "https://github.com/FIWARE-TMForum/DSCUSTOMER.git",
     "branch": "develop",
     "bbdd": "DSCUSTOMER",
     "war": "target/customer.war",
     "root": "DSCustomerManagement",
     "name": "customer",
     "resourcename": "jdbc/customerdbv2"},
    {"url": "https://github.com/FIWARE-TMForum/DSUSAGEMANAGEMENT.git",
     "branch": "develop",
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

charg = {"url": "https://github.com/FIWARE-TMForum/business-ecosystem-charging-backend.git",
         "branch": "develop",
         "name": "charging"}

proxy = {"url": "https://github.com/FIWARE-TMForum/business-ecosystem-logic-proxy.git",
         "branch": "develop"}

def replacement(match):
    field = match.group(2)
    return api.get(field)

with open("./multiDockerTemplate.Dockerfile") as template:
    file = template.read()
    with open("C:\Users\Eugenio\Documents\GitHub\DockerTestingRepo\dockerAPIs\MultiAPIDocker.Dockerfile", 'w+') as dock:
        # Common things to every API on the dockerfile
        dock.write('FROM glassfish\n\n')
        dock.write('RUN apt-get update && apt-get install -y python2.7 python-pip git maven mysql-client\n\n')
        dock.write('# Download the mysql connector and place it in the proper directory\n')
        dock.write('RUN curl http://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.34/mysql-connector-java-5.1.34.jar -o glassfish/lib/mysql-connector-java-5.1.34.jar\n\n')
        dock.write('RUN mkdir wars\n\n')

        for api in APIS:
            dock.write(re.sub(r'(api)-([^ ]+\w)', replacement, file, 4))
with open("C:\Users\Eugenio\Documents\GitHub\DockerTestingRepo\\rssDocker\\rssdocker.Dockerfile") as template:
    file = template.read()
    with open("C:\Users\Eugenio\Documents\GitHub\DockerTestingRepo\\rssDocker\Dockerfile", 'w+') as dock:
        # RSS 
        dock.write(re.sub(r'(api)-([^ ]+\w)', replacement, file, 4))



with open("C:\Users\Eugenio\Documents\GitHub\DockerTestingRepo\dockerAPIs\MultiAPIDocker.Dockerfile", 'a+') as dock:
    dock.write('\nRUN ./bin/asadmin start-domain\n\n')
    dock.write('COPY ./entrypoint.py /\n')
    dock.write('ENTRYPOINT ["./entrypoint.py"]')