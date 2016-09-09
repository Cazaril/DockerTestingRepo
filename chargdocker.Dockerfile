FROM python:2.7

RUN apt-get update && apt-get install -y mongodb python-pip wkhtmltopdf xvfb gcc libxml2-dev libxslt1-dev zlib1g-dev python-dev git maven mysql

RUN git clone https://github.com/FIWARE-TMForum/business-ecosystem-charging-backend.git

WORKDIR business-ecosystem-charging-backend

RUN git checkout develop

ARG PAYPAL_CLIENT_ID
ARG PAYPAL_CLIENT_SECRET

ENV PAYPAL_CLIENT_ID=$PAYPAL_CLIENT_ID
ENV PAYPAL_CLIENT_SECRET=$PAYPAL_CLIENT_SECRET

ENV WORKSPACE=`pwd`

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

# HOST Y PUERTO MISMOS QUE PROXY, RECIBIR POR ENTORNO
RUN ./manage.py createsite external http://127.0.0.1:8000 

RUN ./manage.py createsite internal http://127.0.0.1:8004

# TODO: PASAR A ENTRYPOINT, RECIBIR PARAMS POR ENTORNO/COMANDO, ESTO DEBE SER LO ULTIMO.
# PISAR VARIABLES DE services_settings.py
EXPOSE 8004

RUN ./manage.py runserver 8004 &
