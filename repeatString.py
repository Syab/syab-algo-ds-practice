#!/bin/python3

import math
import os
import random
import re
import sys
import collections


def repeatString(s, n):
    numoccur = 0
    val = n//len(s)
    print(val)
    newstr = (s * (val + 1))
    print(newstr)
    newstr2 = newstr[:n]
    numoccur = newstr2.count('a')
    return numoccur

def repeatedString(s,n):
    numoccur = s.count('a')
    div=n//len(s)
    if n%len(s)==0:
        numoccr= numoccur*div
    else:
        m = n%len(s)
        numoccr= numoccur*div+s[:m].count('a')
    return numoccr

# thestring = input()
# numchar = int(input().strip())

thestring = 'abc'
numchar = 1000000000000

result = repeatedString(thestring, numchar)

print(result)
