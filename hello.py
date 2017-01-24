#!/usr/bin/env python

import os
from pprint import pprint

# print "Content-Type: text/html"
print "Content-Type: text/plain"
print  # Needed to seperate the headers from the body for the http stuff!

pprint( dict(os.environ) )
