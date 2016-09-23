#!/usr/bin/env python

"""
A filter that splits after each word.
"""

import fileinput
import re

def process(line):
	line1 = re.sub('[^A-Za-z0-9]+', ' ', line)
      	for word in line1.split():
			print(word) 


for line in fileinput.input():
    process(line)
