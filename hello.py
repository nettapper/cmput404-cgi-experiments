#!/usr/bin/env python

import os
import json
from pprint import pprint

# print "Content-Type: text/html"
# print "Content-Type: text/plain"
print "Content-Type: application/json"
print  # Needed to seperate the headers from the body for the http stuff!

# pprint(dict(os.environ))
print(json.dumps(dict(os.environ)))
