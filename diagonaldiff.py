#!/bin/python3

import math
import os
import random
import re
import sys
from array import *

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    pdiag=[]
    sdiag=[]
    arrlen=len(arr)
    if (arrlen<=1):
        return(0)
    if (arrlen>1):
        for i in range(arrlen): 
            pdiag.append(arr[i][i])
            sdiag.append(arr[i][arrlen-1-i])
        
        diff=abs(sum(pdiag)-sum(sdiag))
        return(diff)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()