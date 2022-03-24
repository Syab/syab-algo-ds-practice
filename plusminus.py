#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    numneg=0
    numpos=0
    azero=0
    for i in arr:
        print (i)
        if (i == 0) :
            azero = azero+1
        elif (i > 0) :
            numpos= numpos + 1
        elif (i < 0) :
            numneg= numneg+1
    
    print (numpos/len(arr))
    print (numneg/len(arr))
    print (azero/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
