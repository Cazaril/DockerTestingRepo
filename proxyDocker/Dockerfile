FROM ubuntu:14.04

RUN apt-get update && apt-get install -y git python-pip npm wget mongodb

RUN pip install sh

RUN git clone https://github.com/FIWARE-TMForum/business-ecosystem-logic-proxy

WORKDIR business-ecosystem-logic-proxy

RUN wget https://nodejs.org/dist/v4.5.0/node-v4.5.0-linux-x64.tar.xz

RUN tar -xvf node-v4.5.0-linux-x64.tar.xz

RUN echo "export PATH=$PATH:/business-ecosystem-logic-proxy/node-v4.5.0-linux-x64/bin" >> ~/.bashrc

RUN git checkout develop

RUN npm install

RUN cp config.js.template config.js

COPY ./entrypoint.py /
COPY ./entrypoint.sh /


ENTRYPOINT ["/entrypoint.sh"]
