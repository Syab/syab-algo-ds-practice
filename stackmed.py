#!/bin/python3

import math
import os
import random
import re
import sys
import time

def longestbal(str):
    arr=[]
    maxLength =0
    arr.append(-1)

    for i in range(len(str)):
        if str[i] == "(":
            arr.append(i)
            print(arr)
        else:
            arr.pop()
            if len(arr)==0:
                arr.append(i)
            else:
                balancedstr = arr[len(arr) -1]
                currleng = i - balancedstr
                maxLength = max(maxLength, currleng)
                print(arr)
    print(maxLength)



str = input()
longestbal(str)