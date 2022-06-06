#!/bin/python3

import math
import os
import random
import re
import sys

def minindex(myarr, target_num):
    lower = 0
    higher = len(myarr)
    target_num = int(target_num)
    # if target_num not in myarr:
    #     return -1
    # print(type(target_num))
    while lower < higher:
        x = lower + (higher - lower)
        tempval = myarr[x]
        if target_num == tempval:
            return x 
        elif target_num > tempval:
            if lower == x:
                break
            lower = x
        elif target_num < tempval:
            higher = x
    return higher

myarr = input().split()
myarr = list(map(int, myarr))
target_num = input()

print(minindex(myarr, target_num))
