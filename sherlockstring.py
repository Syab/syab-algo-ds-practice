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
    hashmap={}
    sarr=list(s)
    count=0
    for i in sarr:
        if i in hashmap:
            hashmap[i]+= 1
        else:
            hashmap[i]=1
    
    maxofset=max(hashmap.values())
    minofset=min(hashmap.values())
    print(hashmap)
    for j in hashmap:
        if hashmap[j] > minofset:
            count+=1
            if count >= 2:
                print("NO")
                return
        else:
            if maxofset-hashmap[j] == 0 or maxofset-hashmap[j]==1:
                print("YES")
                hashmap.pop(j)
                break
            else:
                print("NO")
                return

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
