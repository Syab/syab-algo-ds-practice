#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    freq = {c:0 for c in s}
    
    for c in s:
        freq[c]+=1
    print(freq)
    freq = list(freq.values())
    freq.sort()
    uniques = [freq[0]]
    
    n = len(freq)
    for i in range(1,n):
        if freq[i]!=freq[i-1]:
            uniques.append(freq[i])
    
    if len(uniques)>2:
        return 'NO'
      
    if len(uniques)!=1:
        w = sum(freq)
        mx = max(freq)
        mn = min(freq)
        if (mn*n)+1!=w and (mx*(n-1))+1!=w:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
