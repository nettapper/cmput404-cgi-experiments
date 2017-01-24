#!/usr/bin/env python

import os
import json
from pprint import pprint
import urlparse
import sys

print "Content-Type: text/html"
# print "Content-Type: text/plain"
# print "Content-Type: application/json"
print  # Needed to seperate the headers from the body for the http stuff!

eVars = dict(os.environ)
# params = urlparse.parse_qs(eVars['QUERY_STRING'])
# userAgent = eVars['HTTP_USER_AGENT']
contentLength = eVars['CONTENT_LENGTH']

username = 'admin'
password = '1234'

# pprint(eVars)
# print("------------")
# print(json.dumps(eVars))
# print("------------")
# print(eVars['QUERY_STRING'])
# print("------------")
# print(params)
# print(userAgent)
# print("------------")
# if 'Fireforx' in userAgent:
#     print("You're using Firefox!")
# elif 'Chrome' in userAgent:
#     print("Your're using Chrome!")
# elif 'curl' in userAgent:
#     print("Your're using Curl!")
# else:
#     print("What you talk'n bout!")

if not contentLength:
  print r"""
      <h1> Welcome! </h1>

      <form method="POST" action="hello.py">
          <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
          <label> <span>Password:</span> <input type="password" name="password"></label>

          <button type="submit"> Login! </button>
      </form>
      """
elif contentLength:
  bytesToRead = int(contentLength)
  content = sys.stdin.read(bytesToRead)
  # print "<pre>", content, "</pre>"
  params = urlparse.parse_qs(content)

  if params['username'][0] == username and params['password'][0] == password:
    print "Hi,", username
  else:
    print "try again.."

