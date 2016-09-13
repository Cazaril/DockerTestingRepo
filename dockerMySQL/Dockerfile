FROM mysql:latest

RUN apt-get update && apt-get install -y python2.7 python-pip

RUN pip install sh

ENV MYSQL_ROOT_PASSWORD=toor

COPY ./entrypoint.sh /

EXPOSE 3306

ENTRYPOINT ["/entrypoint.sh"]
