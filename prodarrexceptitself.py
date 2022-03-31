#!/bin/python3


## NOT SOLVED

from hashlib import new
import math
import os
import random
import re
import sys
import collections

def prodarrayexceptitself(nums, n):
    left = [0]*n
    right = [0]*n
    
    left[0]=1
    right[n-1]=1

    for i in range(1,n): # O(n)
        left[i]=nums[i-1]*left[i-1]
        print(left)
    
    # for j in nums: # O(n)
    #     nres= res//j
    #     newarr.append(nres)
    # return(newarr)

n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
print(prodarrayexceptitself(ar, n))