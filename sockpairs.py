#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    sockset={}
    numpairs=0
    for i in ar:
        if (i in sockset):
            sockset[i]+=1
        else : sockset[i]=1

    for j in list(sockset.keys()):
        numpairs+=(sockset[j]//2)
    
    return(numpairs)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
