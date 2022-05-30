#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Questions = need characters to be as is or need them to be brought ot lower case

mystring = 'abcdefG'

def reversestring(str):
    temp=[]
    for i in range(len(str)-1, 0, -1):  #O(n) solution
        print(str[i])
        temp.append(str[i])
    
    reversedstring=''.join([item for item in temp])
    print(reversedstring)

reversestring(mystring)