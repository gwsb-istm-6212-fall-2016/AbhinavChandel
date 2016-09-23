#!/usr/bin/env python

"""
A filter that removes the stop words.
"""

import fileinput
import re

stopwords = open('stopwords.txt', 'r').read().split()

def process(line):
    line1 = re.sub('[^A-Za-z0-9]+', ' ', line)
    line2=line1.lower().split()
    filteredtext = [t for t in line2 if t.lower() not in stopwords]
    filterline=' '.join(filteredtext)
    print(filterline)
 

for line in fileinput.input():
    process(line)
