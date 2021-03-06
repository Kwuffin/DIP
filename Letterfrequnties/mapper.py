"""
Code is based on the following article
https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
"""

import sys


allowed = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    for i, char in enumerate(line[:-1]):
        char = char.lower()

        # Check first letter
        if char in allowed:
            s1 = char
        else:
            if char == ' ':
                s1 = '#'
            else:
                s1 = '%'

        # Check second letter
        char2 = line[i+1].lower()
        if char2 in allowed:
            s2 = char2
        else:
            if char2 == ' ':
                s2 = '#'
            else:
                s2 = '%'
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1

        print('%s-%s\t%s' % (s1, s2, 1))
