#!/usr/bin/env python
from os import getenv, system
from sh import sed
from pymongo import MongoClient
import sys, time

#sys.path = ["/business-ecosystem-charging-backend/src/"] + sys.path

#for p in sys.path:
#    print(p)

# Connect to mongodb
connection = MongoClient(connect=False)
# use wstore_context
db = connection['wstore_db']  

connected = False

while not connected:
    try:
        print("\nTesting connection to mongodb\n")
        time.sleep(0.5)
        dbNames = db.collection_names()
        connected = True
    except:
        pass

if not connected:
    print("Cant stablish connection to mongodb\n")
    sys.exit()
    
try:
    if "site" not in dbNames:
        system("/business-ecosystem-charging-backend/src/manage.py createsite external {}:{}".format(getenv("BIZ_ECOSYS_HOST"), getenv("BIZ_ECOSYS_PORT")))
except:
    print("ERROR CREATESITE EXTERNAL")
    sys.exit()

try:
    if "local_site" not in db.collection_names():
        system("/business-ecosystem-charging-backend/src/manage.py createsite internal http://127.0.0.1:8004")
except:
    print("ERROR CREATESITE INTERNAL")
    sys.exit()
#print(dbNames)
