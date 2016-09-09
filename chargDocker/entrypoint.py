#!/usr/bin/env python

from os import getenv, system
from sh import sed
from pymongo import Connection
import sys, time


if getenv("PAYPAL_CLIENT_ID") is None:
    print("PAYPAL_CLIENT_ID environment variable not set")
    sys.exit()
    
if getenv("PAYPAL_CLIENT_SECRET") is None:
    print("PAYPAL_CLIENT_SECRET environment variable not set")
    sys.exit()

if getenv("BIZ_ECOSYS_PORT") is None:
    print("BIZ_ECOSYS_PORT environment variable not set")
    sys.exit()

if getenv("BIZ_ECOSYS_HOST") is None:
    print("BIZ_ECOSYS_HOST environment variable not set")
    sys.exit()

# Change the paypal credentials
sed("-i", 's/PAYPAL_CLIENT_ID = \'[\w-]*\'/PAYPAL_CLIENT_ID = getenv\(\'PAYPAL_CLIENT_ID\'\)/g', "./wstore/charging_engine/payment_client/paypal_client.py")

sed("-i", 's/PAYPAL_CLIENT_SECRET = \'[\w-]*\'/PAYPAL_CLIENT_SECRET = getenv\(\'PAYPAL_CLIENT_SECRET\'\)/g', "./wstore/charging_engine/payment_client/paypal_client.py")

sed("-i", 's/from os import path/from os import sh, getenv/g', "./settings.py") 

sed("-i", 's/WSTOREMAIL = \'\<email\>\'/getenv\(\'WSTOREMAIL\', \<email\>\)/g', "./settings.py")

sed("-i", 's/WSTOREMAILUSER = \'\<mail_user\'/getenv\(\'WSTOREMAILUSER\', \<user\>\)/g', "./settings.py")

sed("-i", 's/WSTOREMAILPASS = \'\<email_passwd\>\'/getenv\(\'WSTOREMAILPASS\', \<email_passwd\>\)/g', "./settings.py")

sed("-i", 's/PAYMENT_METHOD = None/ PAYMENT_METHOD = paypal/g', "./settings.py")

sed("-i", "s|INVENTORY = 'http://localhost:8080/DSProductInventory'|INVENTORY = 'http://${BIZ_ECOSYS_HOST}:${BIZ_ECOSYS_PORT}/DSProductInventory'|g", "services_settings.py")

sed("-i", "s|ORDERING = 'http://localhost:8080/DSProductOrdering'|ORDERING = 'http://${BIZ_ECOSYS_HOST}:${BIZ_ECOSYS_PORT}/ORDERING'|g", "services_settings.py")

sed("-i", "s|BILLING = 'http://localhost:8080/DSBillingManagement'|BILLING = 'http://${BIZ_ECOSYS_HOST}:${BIZ_ECOSYS_PORT}/BILLING'|g", "services_settings.py")

sed("-i", "s|RSS = 'http://localhost:8080/DSRevenueSharing'|RSS = http://${BIZ_ECOSYS_HOST}:${BIZ_ECOSYS_PORT}/RSS'|g", "services_settings.py")

sed("-i", "s/USAGE = 'http://localhost:8080/DSUsageManagement'/USAGE = 'http://${BIZ_ECOSYS_HOST}:${BIZ_ECOSYS_PORT}/USAGE/'g", "services_settings.py")

sed("-i", "s/AUTHORIZE_SERVICE = 'http://localhost:8004/authorizeService/apiKeys'/AUTHORIZE_SERVICE = 'http://${BIZ_ECOSYS_HOST}:${BIZ_ECOSYS_PORT}/AUTHORIZE_SERVICE'/g", "services_settings.py")


# Connect to mongodb
connection = Connection('localhost', 27017)
# use wstore_context
db = connection['wstore_context']  


if "site" not in db.collection_names():
    system("./manage.py createsite external {}:{}".format(getenv("BIZ_ECOSYS_HOST"), getenv("BIZ_ECOSYS_PORT")))

if "local_site" not in db.collection_names():
    system("./manage.py createsite internal http://127.0.0.1:8004")

system("./manage.py runserver 8004 &")
