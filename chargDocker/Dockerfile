FROM python:2.7

RUN apt-get update && apt-get install -y mongodb python-dev git 

RUN git clone https://github.com/FIWARE-TMForum/business-ecosystem-charging-backend.git

RUN pip install sh

WORKDIR business-ecosystem-charging-backend

RUN git checkout develop

ENV WORKSPACE=`pwd`

RUN ./python-dep-install.sh

WORKDIR src

RUN mkdir -p /data/db/

COPY ./entrypoint.py /
COPY ./entrypoint.sh /

EXPOSE 8004

ENTRYPOINT ["/entrypoint.sh"]