FROM mysql:latest

RUN apt-get update && apt-get install -y python2.7 python-pip

RUN pip install sh

ENV MYSQL_ROOT_PASSWORD=toor

COPY ./sql_schema.sql /

COPY ./entrypoint.py /

EXPOSE 3306

ENTRYPOINT ["/entrypoint.py"]
