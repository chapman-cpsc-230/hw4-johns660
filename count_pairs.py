"""
File: <count_pairs>

Copyright (c) 2016 <Lindsey Johnson>

License: MIT

<makes the computer count how many pairs there are and then print the number.>
"""

def countPairs(dna, pair):
    pairs = 0

    i = 0
    while (i < len(dna)):
        index = dna.find(pair, i)
        if (index != -1):
            pairs += 1
            i = index
        i += 1

    print "There are", pairs, "pairs!"


countPairs("AGTAGGGTGATA", "AG")
