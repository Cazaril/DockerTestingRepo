FROM glassfish

RUN apt-get update && apt-get install -y python2.7

# Download the mysql connector and place it in the proper directory
RUN curl http://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.34/mysql-connector-java-5.1.34.jar -o glassfish/lib/mysql-connector-java-5.1.34.jar

RUN git clone https://github.com/FIWARE-TMForum/DSUSAGEMANAGEMENT.git 

WORKDIR DSUSAGEMANAGEMENT 

RUN git checkout develop

# Create WAR file
RUN mvn install

# Fixing reloading the database everytime the API is restarted
RUN \
    sed -i 's/<provider>org\.eclipse\.persistence\.jpa\.PersistenceProvider<\/provider>/ /g' ./src/main/resources/META-INF/persistence.xml \
    sed -i 's/<property name="eclipselink\.ddl-generation" value="drop-and-create-tables"\/>/ /g' ./src/main/resources/META-INF/persistence.xml \
    sed -i 's/<property name="eclipselink\.logging\.level" value="FINE"\/>/ /g' ./src/main/resources/META-INF/persistence.xml

# Create DATABASE
RUN mysql -u toor -proot -e CREATE DATABASE IF NOT EXISTS DSUSAGEMANAGEMENT;

# Create Pool
RUN asadmin create-jdbc-connection-pool --restype java.sql.Driver --driverclassname com.mysql.jdbc.Driver --property 
'user=root:password=toor:URL="jdbc:mysql://localhost:3306/DSUSAGEMANAGEMENT"' DSUSAGEMANAGEMENT 

# Create Resource
RUN asadmin create-jdbc-resource --connectionpoolid jdbc/usagedbv2 DSUSAGEMANAGEMENT 

# Deploy the application
RUN asadmin deploy --contextroot DSUsageManagement --name DSUsageManagement target/usageManagement.war  
