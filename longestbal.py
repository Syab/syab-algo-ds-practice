#!/bin/python3

from hashlib import new
import math
from operator import attrgetter
import os
import random
import re
import sys
import time

"""
iterate through str
))))))((()))
"""

def longestbal(str):
    stckarr = []
    stckarr.append(-1) # WHY?
    strlen = len(str)
    count=0

    for i in range(strlen):
        if (i == "(" ):
            stckarr.append(i)
        else:
            stckarr.pop()
            if (len(stckarr) == 0):
                stckarr.append(i)
            else:
                count=max(count, i - stckarr[len(stckarr)-1])
    return (count)

str = input()
print(longestbal(str))