"""
Code is based on the following article
https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
"""

import sys
import re


allowed = re.compile('[^a-zA-Z]')
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    for i, char in enumerate(line[:-1]):
        char = char.lower()

        # Check first letter
        if char.isalpha():
            s1 = char
        else:
            if char == ' ':
                s1 = '#'
            else:
                s1 = '%'

        # Check second letter
        if line[i+1].isalpha():
            s2 = line[i+1]
        else:
            if line[i+1] == ' ':
                s2 = '#'
            else:
                s2 = '%'
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print('%s-%s\t%s' % (s1, s2, 1))
