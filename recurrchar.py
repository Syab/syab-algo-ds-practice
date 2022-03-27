#!/bin/python3

from hashlib import new
import math
import os
import random
import re
import sys
import time

# o(1) solution as hashmap acess and insert is O(1)

newarr=['a', 'h', 'g', 'j', 'j', 'k']

def findFirstRecurr(a):
    newhash={}
    for i in a:
        print(newhash)
        if (i in newhash):
            print("{} is the first recurring character".format(i))
        else:
            newhash[i]=0

findFirstRecurr(newarr)