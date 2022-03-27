#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    arrset={}
    for i in a:
        if (i in arrset):
            arrset[i]+=1
        else:
            arrset[i]=1
    for e in arrset:
        if (arrset[e] == 1):
            return(e)
    
    # print(arrset)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # result = lonelyinteger(a)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    lonelyinteger(a)