#!/bin/python3

import math
import os
import random
import re
import sys

# Assumptions to ask : 
# is the array ordered? or can they be unordered
# max value of each element in the array
# are they integers or can they be decimeals (float/doubles)
# find duplicates - if duplicate, omit 1 or both duplicates

def miniMaxSum(arr):
    # Write your code here
    maxele=max(arr)
    minele=min(arr)
    maxsum=sum(arr)-minele #O(1)
    minsum=sum(arr)-maxele #O(1)
    print (minsum , maxsum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
