#!/usr/bin/env python

import clearbit
import json
import sys

clearbit.key = 'sk_c116bb2548cbf0cf36ab39503cc5cf5e'

if len(sys.argv) < 2:
  sys.exit('Usage: cli.py [email]')

email = sys.argv[1]
lookup = clearbit.Enrichment.find(email=email, stream=True)

if lookup != None:
  print(json.dumps(lookup['person'], sort_keys=True, indent=4))
  print(json.dumps(lookup['company'], sort_keys=True, indent=4))
else:
  print('Email not found')
