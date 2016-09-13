FROM glassfish

RUN apt-get update && apt-get install -y wkhtmltopdf xvfb gcc libxml2-dev libxslt1-dev zlib1g-dev python-dev python2.7 python-pip git maven

RUN pip install sh

# Download the mysql connector and place it in the proper directory
RUN wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.39.tar.gz

RUN tar -xvf mysql-connector-java-5.1.39.tar.gz

RUN cp ./mysql-connector-java-5.1.39/mysql-connector-java-5.1.39-bin.jar glassfish/domains/domain1/lib

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

COPY ./entrypoint.py /

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
