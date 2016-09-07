#!/usr/bin/env python
# Credits of this code to @Rock_Neurotiko
from os import getenv
import sys
from sh import asadmin

rss = {"url": "https://github.com/FIWARE-TMForum/business-ecosystem-rss.git",
       "branch": "develop",
       "bbdd": "RSS",
       "war": "fiware-rss/target/DSRevenueSharing.war",
       "name": "rss",
       "root": "DSRevenueSharing"}

if getenv("RSS_CLIENT_ID") is None:
    print("RSS_CLIENT_ID is not set")
    sys.exit()

if getenv("RSS_SECRET") is None:
    print("RSS_SECRET is not set")
    sys.exit()

if getenv("RSS_URL") is None:
    print("RSS_URL is not set")
    sys.exit()

text = ""
with open("/etc/default/rss/oauth.properties") as f:
    text = f.read()
text = text.replace("config.client_id=", "config.client_id={}".format(getenv("RSS_CLIENT_ID")))
text = text.replace("config.client_secret=", "config.client_secret={}".format(getenv("RSS_SECRET")))
text = text.replace("config.callbackURL=", "config.callbackURL={}/fiware-rss/callback".format(getenv('RSS_URL')))
with open("/etc/default/rss/oauth.properties", "w") as f:
    f.write(text)


asadmin("deploy", "--force", "true" if force else "false", "--contextroot", rss.get('root'), "--name", rss.get('root'), rss.get('war'))

