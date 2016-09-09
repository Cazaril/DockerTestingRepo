#!/usr/bin/env python
from sh import sed
from os import getenv, system
import sys

if getenv("OAUTH2_CLIENT_ID") is None:
    print("environment variable OAUTH2_CLIENT_ID not set")
    sys.exit()
    
if getenv("OAUTH2_CLIENT_SECRET") is None:
    print("environment variable OAUTH2_CLIENT_SECRET not set")
    sys.exit()

params = [
    {'matchpath': "'path': ''",
     'path': "'path': 'DSProductCatalog' ",
     'matchport': "'port': ''",
     'port': "'port': '{}'".format(getenv('GLASSFISH_PORT'))
    },
    {'matchpath': "'path': ''",
     'path': "'path': 'DSProductOrdering'",
     'matchport': "'port': ''",
     'port': "'port': '{}'".format(getenv('GLASSFISH_PORT'))
    },
    {'matchpath': "'path': ''",
     'path': "'path': 'DSProductInventory'",
     'matchport': "'port': ''",
     'port': "'port': '{}'".format(getenv('GLASSFISH_PORT'))
    },
    {'matchpath': "'path': ''",
     'path': "'path': 'DSPartyManagement'",
     'matchport': "'port': ''",
     'port': "'port': '{}'".format(getenv('GLASSFISH_PORT'))
    },
    {'matchpath': "'path': ''",
     'path': "'path': 'DSBillingManagement'",
     'matchport': "'port': ''",
     'port': "'port': '{}'".format(getenv('GLASSFISH_PORT'))
    },
    {'matchpath': "'path': ''",
     'path': "'path': 'DSCustomerManagement'",
     'matchport': "'port': ''",
     'port': "'port': '{}'".format(getenv('GLASSFISH_PORT'))
    },
    {'matchpath': "'path': ''",
     'path': "'path': 'charging'",
     'matchport': "'port': ''",
     'port': "'port': '{}'".format(getenv('GLASSFISH_PORT'))
    },
    {'matchpath': "'path': ''",
     'path': "'path': 'DSRevenueSharing'",
     'matchport': "'port': ''",
     'port': "'port': '{}'".format(getenv('GLASSFISH_PORT'))
    },
    {'matchpath': "'path': ''",
     'path': "'path': 'DSUsageManagement'",
     'matchport': "'port': ''",
     'port': "'port': '{}'".format(getenv('GLASSFISH_PORT'))}]

port = {'matchport': "config.port = 80;",
        'port': "config.port = {};".format(getenv("BIZ_ECOSYS_PORT", "80"))}
prefix = {'matchprefix': "config.proxyPrefix = '/proxy';",
          'prefix': 'config.proxyPrefix = ""'}
app = {'matchapp': "config.appHost = '';",
          'port': 'config.appHost = "127.0.0.1"'}

text = ""
with open("./config.js") as f:
    text = f.read()


for change in params:
    text = text.replace(change.get('matchpath'), change.get('path'), 1)
    text = text.replace(change.get('matchport'), change.get('port'), 1)


print(getenv("OAUTH2_CLIENT_SECRET"))
print(getenv("OAUTH2_CLIENT_ID"))
text = text.replace(port.get('matchport'), port.get('port'))
text = text.replace(prefix.get('matchprefix'), prefix.get('prefix'))
text = text.replace(app.get('matchapp'), app.get('port'))
text = text.replace("'clientSecret': '--client-secret--',", "'clientSecret': '{}',".format(getenv("OAUTH2_CLIENT_SECRET")))
text = text.replace("'clientID': '--client-id--',", "'clientID': '{}',".format(getenv("OAUTH2_CLIENT_ID")))
text = text.replace("'callbackURL': '--callback-url--',", "'callbackURL': 'http://{}:{}/auth/fiware/callback',".format(getenv("BIZ_ECOSYS_HOST"), getenv("BIZ_ECOSYS_PORT")))

print(text)
with open("./config.js", "w+") as f:
    f.write(text)
    print("ESTO ES EL FICHERO")
    print(f.read())

    
system("service mongodb start")

system("/business-ecosystem-logic-proxy/node-v4.5.0-linux-x64/bin/node server.js")
