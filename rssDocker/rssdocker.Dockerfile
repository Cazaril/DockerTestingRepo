FROM glassfish

RUN apt-get update && apt-get install -y python2.7 python-pip git maven mysql-client

RUN pip install sh

# Consume parameters
ARG RSS_URL 
ARG RSS_SECRET 
ARG RSS_CLIENT_ID

ENV RSS_URL=$RSS_URL
ENV RSS_SECRET=$RSS_SECRET
ENV RSS_CLIENT_ID=$RSS_CLIENT_ID

RUN git clone https://github.com/FIWARE-TMForum/business-ecosystem-rss.git

WORKDIR business-ecosystem-rss

RUN git checkout develop

# Create WAR file

RUN mvn install -DskipTests

RUN mkdir /etc/default/rss/

RUN cp ./properties/database.properties /etc/default/rss/database.properties

RUN cp ./properties/oauth.properties /etc/default/rss/oauth.properties

RUN sed -i 's/jdbc:mysql:\/\/localhost:3306\/RSS/jdbc:mysql:\/\/root:3306\/RSS/g' /etc/default/rss/database.properties

RUN sed -i 's/database.password=root/database.password=toor/g' /etc/default/rss/database.properties

RUN echo 'config.sellerRole=seller' >> /etc/default/rss/oauth.properties

RUN echo 'config.aggregatorRole=aggregator' >> /etc/default/rss/oauth.properties

COPY ./entrypoint.py /
ENTRYPOINT ["/entrypoint.py"]