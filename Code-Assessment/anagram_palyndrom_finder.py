#!/usr/bin/env python

from urllib.request import urlopen

with urlopen('https://www.wikidata.org/wiki/Q13417213') as webpage:
    content = webpage.read().decode()

print(content)