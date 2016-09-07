FROM glassfish

RUN apt-get update && apt-get install -y mongodb wkhtmltopdf xvfb gcc libxml2-dev libxslt1-dev zlib1g-dev python-dev python2.7 python-pip git maven

RUN pip install sh

# Download the mysql connector and place it in the proper directory
RUN curl http://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.34/mysql-connector-java-5.1.34.jar -o glassfish/lib/mysql-connector-java-5.1.34.jar

RUN mkdir wars

RUN git clone https://github.com/FIWARE-TMForum/DSPRODUCTCATALOG2.git
 
WORKDIR DSPRODUCTCATALOG2 

RUN git checkout master

# Create WAR file
RUN mvn install

RUN mv ./target/DSPRODUCTCATALOG2.war ../wars/

# Fixing reloading the database everytime the API is restarted
RUN sed -i 's/jdbc\/sample/jdbc\/pcatv2/g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<provider>org\.eclipse\.persistence\.jpa\.PersistenceProvider<\/provider>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.ddl-generation" value="drop-and-create-tables"\/>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.logging\.level" value="FINE"\/>/ /g' ./src/main/resources/META-INF/persistence.xml

RUN if [ -f "./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties" ]; then mv ./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties ./DSPRODUCTORDERING/src/main/resources/settings.properties; fi

# Add condition if not present in properties. This was as pain to write as it is to read
RUN grep -F "<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"/>" ./src/main/resources/META-INF/persistence.xml || sed -i 's/<\/properties>/\t<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"\/>\n\t\t<\/properties>/g' ./src/main/resources/META-INF/persistence.xml

WORKDIR ../

# Next api Docker
RUN git clone https://github.com/FIWARE-TMForum/DSPRODUCTORDERING.git
 
WORKDIR DSPRODUCTORDERING 

RUN git checkout develop

# Create WAR file
RUN mvn install

RUN mv ./target/productOrdering.war ../wars/

# Fixing reloading the database everytime the API is restarted
RUN sed -i 's/jdbc\/sample/jdbc\/pcatv2/g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<provider>org\.eclipse\.persistence\.jpa\.PersistenceProvider<\/provider>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.ddl-generation" value="drop-and-create-tables"\/>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.logging\.level" value="FINE"\/>/ /g' ./src/main/resources/META-INF/persistence.xml

RUN if [ -f "./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties" ]; then mv ./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties ./DSPRODUCTORDERING/src/main/resources/settings.properties; fi

# Add condition if not present in properties. This was as pain to write as it is to read
RUN grep -F "<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"/>" ./src/main/resources/META-INF/persistence.xml || sed -i 's/<\/properties>/\t<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"\/>\n\t\t<\/properties>/g' ./src/main/resources/META-INF/persistence.xml

WORKDIR ../

# Next api Docker
RUN git clone https://github.com/FIWARE-TMForum/DSPRODUCTINVENTORY.git
 
WORKDIR DSPRODUCTINVENTORY 

RUN git checkout develop

# Create WAR file
RUN mvn install

RUN mv ./target/productInventory.war ../wars/

# Fixing reloading the database everytime the API is restarted
RUN sed -i 's/jdbc\/sample/jdbc\/pcatv2/g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<provider>org\.eclipse\.persistence\.jpa\.PersistenceProvider<\/provider>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.ddl-generation" value="drop-and-create-tables"\/>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.logging\.level" value="FINE"\/>/ /g' ./src/main/resources/META-INF/persistence.xml

RUN if [ -f "./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties" ]; then mv ./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties ./DSPRODUCTORDERING/src/main/resources/settings.properties; fi

# Add condition if not present in properties. This was as pain to write as it is to read
RUN grep -F "<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"/>" ./src/main/resources/META-INF/persistence.xml || sed -i 's/<\/properties>/\t<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"\/>\n\t\t<\/properties>/g' ./src/main/resources/META-INF/persistence.xml

WORKDIR ../

# Next api Docker
RUN git clone https://github.com/FIWARE-TMForum/DSPARTYMANAGEMENT.git
 
WORKDIR DSPARTYMANAGEMENT 

RUN git checkout develop

# Create WAR file
RUN mvn install

RUN mv ./target/party.war ../wars/

# Fixing reloading the database everytime the API is restarted
RUN sed -i 's/jdbc\/sample/jdbc\/pcatv2/g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<provider>org\.eclipse\.persistence\.jpa\.PersistenceProvider<\/provider>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.ddl-generation" value="drop-and-create-tables"\/>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.logging\.level" value="FINE"\/>/ /g' ./src/main/resources/META-INF/persistence.xml

RUN if [ -f "./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties" ]; then mv ./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties ./DSPRODUCTORDERING/src/main/resources/settings.properties; fi

# Add condition if not present in properties. This was as pain to write as it is to read
RUN grep -F "<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"/>" ./src/main/resources/META-INF/persistence.xml || sed -i 's/<\/properties>/\t<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"\/>\n\t\t<\/properties>/g' ./src/main/resources/META-INF/persistence.xml

WORKDIR ../

# Next api Docker
RUN git clone https://github.com/FIWARE-TMForum/DSBILLINGMANAGEMENT.git
 
WORKDIR DSBILLINGMANAGEMENT 

RUN git checkout develop

# Create WAR file
RUN mvn install

RUN mv ./target/billingManagement.war ../wars/

# Fixing reloading the database everytime the API is restarted
RUN sed -i 's/jdbc\/sample/jdbc\/pcatv2/g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<provider>org\.eclipse\.persistence\.jpa\.PersistenceProvider<\/provider>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.ddl-generation" value="drop-and-create-tables"\/>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.logging\.level" value="FINE"\/>/ /g' ./src/main/resources/META-INF/persistence.xml

RUN if [ -f "./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties" ]; then mv ./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties ./DSPRODUCTORDERING/src/main/resources/settings.properties; fi

# Add condition if not present in properties. This was as pain to write as it is to read
RUN grep -F "<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"/>" ./src/main/resources/META-INF/persistence.xml || sed -i 's/<\/properties>/\t<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"\/>\n\t\t<\/properties>/g' ./src/main/resources/META-INF/persistence.xml

WORKDIR ../

# Next api Docker
RUN git clone https://github.com/FIWARE-TMForum/DSCUSTOMER.git
 
WORKDIR DSCUSTOMER 

RUN git checkout develop

# Create WAR file
RUN mvn install

RUN mv ./target/customer.war ../wars/

# Fixing reloading the database everytime the API is restarted
RUN sed -i 's/jdbc\/sample/jdbc\/pcatv2/g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<provider>org\.eclipse\.persistence\.jpa\.PersistenceProvider<\/provider>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.ddl-generation" value="drop-and-create-tables"\/>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.logging\.level" value="FINE"\/>/ /g' ./src/main/resources/META-INF/persistence.xml

RUN if [ -f "./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties" ]; then mv ./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties ./DSPRODUCTORDERING/src/main/resources/settings.properties; fi

# Add condition if not present in properties. This was as pain to write as it is to read
RUN grep -F "<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"/>" ./src/main/resources/META-INF/persistence.xml || sed -i 's/<\/properties>/\t<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"\/>\n\t\t<\/properties>/g' ./src/main/resources/META-INF/persistence.xml

WORKDIR ../

# Next api Docker
RUN git clone https://github.com/FIWARE-TMForum/DSUSAGEMANAGEMENT.git
 
WORKDIR DSUSAGEMANAGEMENT 

RUN git checkout develop

# Create WAR file
RUN mvn install

RUN mv ./target/usageManagement.war ../wars/

# Fixing reloading the database everytime the API is restarted
RUN sed -i 's/jdbc\/sample/jdbc\/pcatv2/g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<provider>org\.eclipse\.persistence\.jpa\.PersistenceProvider<\/provider>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.ddl-generation" value="drop-and-create-tables"\/>/ /g' ./src/main/resources/META-INF/persistence.xml 
RUN sed -i 's/<property name="eclipselink\.logging\.level" value="FINE"\/>/ /g' ./src/main/resources/META-INF/persistence.xml

RUN if [ -f "./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties" ]; then mv ./DSPRODUCTORDERING/src/main/java/org/tmf/dsmapi/settings.properties ./DSPRODUCTORDERING/src/main/resources/settings.properties; fi

# Add condition if not present in properties. This was as pain to write as it is to read
RUN grep -F "<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"/>" ./src/main/resources/META-INF/persistence.xml || sed -i 's/<\/properties>/\t<property name=\"javax.persistence.schema-generation.database.action\" value=\"drop-and-create\"\/>\n\t\t<\/properties>/g' ./src/main/resources/META-INF/persistence.xml

WORKDIR ../

# Next api Docker
# Next api Docker
RUN pip install sh

# Consume parameters
ARG RSS_URL 
ARG RSS_SECRET 
ARG RSS_CLIENT_ID

ENV RSS_URL=$RSS_URL
ENV RSS_SECRET=$RSS_SECRET
ENV RSS_CLIENT_ID=$RSS_CLIENT_ID

RUN git clone https://github.com/FIWARE-TMForum/business-ecosystem-rss.git

RUN git checkout develop

WORKDIR business-ecosystem-rss

# Create WAR file

RUN mvn install -DskipTests

RUN mv ./fiware-rss/target/DSRevenueSharing.war ../wars/

RUN mkdir /etc/default/rss/

RUN cp ./properties/database.properties /etc/default/rss/database.properties

RUN cp ./properties/oauth.properties /etc/default/rss/oauth.properties

RUN sed -i 's/jdbc:mysql:\/\/localhost:3306\/RSS/jdbc:mysql:\/\/root:3306\/RSS/g' /etc/default/rss/database.properties

RUN sed -i 's/database.password=root/database.password=toor/g' /etc/default/rss/database.properties

RUN echo 'config.sellerRole=seller' >> /etc/default/rss/oauth.properties

RUN echo 'config.aggregatorRole=aggregator' >> /etc/default/rss/oauth.properties

WORKDIR ../
# Next api Docker
RUN git clone https://github.com/FIWARE-TMForum/business-ecosystem-charging-backend.git

WORKDIR business-ecosystem-charging-backend

RUN git checkout develop

ARG PAYPAL_CLIENT_ID
ARG PAYPAL_CLIENT_SECRET

ENV PAYPAL_CLIENT_ID=$PAYPAL_CLIENT_ID
ENV PAYPAL_CLIENT_SECRET=$PAYPAL_CLIENT_SECRET

ENV WORKSPACE=`pwd`

RUN virtualenv virtenv

RUN source virtenv/bin/activate

RUN ./python-dep-install.sh

WORKDIR src

RUN if [ -z "${PAYPAL_CLIENT_ID+x}" ]; then exit 1;

RUN if [ -z "${PAYPAL_CLIENT_SECRET+x}" ]; then exit 1;

# Change the paypal credentials
RUN sed -i 's/PAYPAL_CLIENT_ID = \'[\w-]*\'/PAYPAL_CLIENT_ID = getenv\(\'PAYPAL_CLIENT_ID\'\)/g' ./wstore/charging_engine/payment_client/paypal_client.py

RUN sed -i 's/PAYPAL_CLIENT_SECRET = \'[\w-]*\'/PAYPAL_CLIENT_SECRET = getenv\(\'PAYPAL_CLIENT_SECRET\'\)/g' ./wstore/charging_engine/payment_client/paypal_client.py

RUN sed -i 's/from os import path/from os import sh, getenv/g' ./settings.py 

RUN sed -i 's/WSTOREMAIL = \'\<email\>\'/getenv\(\'WSTOREMAIL\', \<email\>\)/g' ./settings.py

RUN sed -i 's/PAYMENT_METHOD = None/ PAYMENT_METHOD = paypal/g' ./settings.py 

RUN ./manage.py createsite external http://127.0.0.1:8000

RUN ./manage.py createsite internal http://127.0.0.1:8004

RUN ./manage.py runserver 8004 &

WORKDIR ../../

RUN ./bin/asadmin start-domain

COPY ./entrypoint.py /
ENTRYPOINT ["./entrypoint.py"]