FROM mysql:latest

RUN apt-get update

# Create DATABASE
RUN mysql -u root -ptoor -e CREATE DATABASE IF NOT EXISTS DSPRODUCTCATALOG2;

# Create DATABASE
RUN mysql -u root -ptoor -e CREATE DATABASE IF NOT EXISTS DSPRODUCTORDERING;

# Create DATABASE
RUN mysql -u root -ptoor -e CREATE DATABASE IF NOT EXISTS DSPRODUCTINVENTORY;

# Create DATABASE
RUN mysql -u root -ptoor -e CREATE DATABASE IF NOT EXISTS DSPARTYMANAGEMENT;

# Create DATABASE
RUN mysql -u root -ptoor -e CREATE DATABASE IF NOT EXISTS DSBILLINGMANAGEMENT;

# Create DATABASE
RUN mysql -u root -ptoor -e CREATE DATABASE IF NOT EXISTS DSCUSTOMER;

# Create DATABASE
RUN mysql -u root -ptoor -e CREATE DATABASE IF NOT EXISTS DSUSAGEMANAGEMENT;

RUN mysql -u root -ptoor -e CREATE DATABASE IF NOT EXISTS RSS;

EXPOSE 3306