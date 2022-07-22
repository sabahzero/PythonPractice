#!/usr/bin/env python

from urllib.request import urlopen

with urlopen('https://www.wikidata.org/wiki/Q13417213') as webpage: # Adjust to be any URL (selected page with palindromes)
    content = webpage.read().decode()
    # convert content to be strings in a csv with 3 columns (string, anagram, palindrome)
    # which strings are anagrams of each other: True of False (update 2nd column of csv)
    # which strings are palindromes: True or False (update 3rd column of csv)
    # update to be final csv for easy readability for user (hypothetical of nucleotides and reverse compliments)

print(content)