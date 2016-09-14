FROM mysql:latest

RUN apt-get update

# ENV MYSQL_ROOT_PASSWORD=toor

COPY ./entrypoint.sh /

EXPOSE 3306

ENTRYPOINT ["/entrypoint.sh"]
