#!/usr/bin/env python

"""
A filter that converts upper case into lower case.
"""

import fileinput


def process(line):
    print(line.lower())


for line in fileinput.input():
    process(line)
