#!/usr/bin/env python

import os
import json
from pprint import pprint
import urlparse

# print "Content-Type: text/html"
print "Content-Type: text/plain"
# print "Content-Type: application/json"
print  # Needed to seperate the headers from the body for the http stuff!

# pprint(dict(os.environ))

eVars = dict(os.environ)
params = urlparse.parse_qs(eVars['QUERY_STRING'])

# print(json.dumps(eVars))
# print("------------")
# print(eVars['QUERY_STRING'])
# print("------------")
print(params)
