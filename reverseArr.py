#!/bin/python3

import math
import os
import random
import re
import sys
import collections

def reverseArray(n,ar):
    revArr = ar[::-1]
    # print(revArr)
    for i in range(0, n):
        print (i)
        

n = int(input().strip())
ar = []
for i in range(0, n):
    ar.append(int(input()))

result= reverseArray(n,ar)

# print(result)