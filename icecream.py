#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    # tempdict = {}
    # for i in range(len(arr)):
    #     if arr[i] in tempdict:
    #         print([tempdict[arr[i]]+1, i+1])
    #     else:
    #         diff = m - arr[i]
    #         tempdict[diff] = 1
        # rem = m - i
        # if rem in arr:
        #     return([arr.index(i)+1, arr.index(rem)+1])
    temp_dict = {}
    for i in range(len(arr)):
        if arr[i] in temp_dict:
            print([temp_dict[arr[i]]+1, i+1])
            return [temp_dict[arr[i]]+1, i+1]
        else:
            diff = m - arr[i]
            temp_dict[diff] = i

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')

    # fptr.close()