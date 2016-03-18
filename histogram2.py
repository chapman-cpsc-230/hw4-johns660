"""
File: <histogram2>

Copyright (c) 2016 <Lindsey Johnson>

License: MIT

<An enhanced version of the historgram with a title and header. This program uses the digits code to print stars. So it essentially just prints stars for how many digits there are in the number.>
"""


def digits(n):
    return len(str(n))



def histogram2(name, tup):
        print"n | " + name
        print "__________________"
        for i in tup:
            stars = []
            for x in range(digits(i)):
                stars.append('*')
            s = ''.join(stars)
            print digits(i), "| ", s

histogram2("Data", [4, 33, 523, 62, 6])
