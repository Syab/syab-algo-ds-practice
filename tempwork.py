#!/bin/python3

import math
import os
import random
import re
import sys

arr = [1,2,3,4,5]
arrtwo=['art','colour','friend','orange']
s="hehhhhlo"

print(arrtwo.index('art'))

def isValid(s):
    # Write your code here
    freq = {c:0 for c in s}
    print(s)