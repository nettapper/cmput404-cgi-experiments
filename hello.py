#!/usr/bin/env python

import os
import json
from pprint import pprint
import urlparse

# print "Content-Type: text/html"
print "Content-Type: text/plain"
# print "Content-Type: application/json"
print  # Needed to seperate the headers from the body for the http stuff!

eVars = dict(os.environ)
params = urlparse.parse_qs(eVars['QUERY_STRING'])
userAgent = eVars['HTTP_USER_AGENT']

# pprint(eVars)
# print("------------")
# print(json.dumps(eVars))
# print("------------")
# print(eVars['QUERY_STRING'])
# print("------------")
print(params)
print(userAgent)
print("------------")
if 'Fireforx' in userAgent:
    print("You're using Firefox!")
elif 'Chrome' in userAgent:
    print("Your're using Chrome!")
elif 'curl' in userAgent:
    print("Your're using Curl!")
else:
    print("What you talk'n bout!")
