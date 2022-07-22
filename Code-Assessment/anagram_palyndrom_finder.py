#!/usr/bin/env python

from urllib.request import urlopen

with urlopen() as webpage:
    content = webpage.read().decode()

print(content)