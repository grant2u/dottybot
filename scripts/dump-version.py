#!/usr/bin/env python

import json

with open('config.json', 'r') as fh:
    config = json.load(fh)

print(config['version'])
