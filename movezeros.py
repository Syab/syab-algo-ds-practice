#!/bin/python3

import math
import os
import random
import re
import sys
import collections
import itertools

def move_zeros_to_left(A):
    wozero=[]
    wzero=[]
    for i in A:
        if(i ==0):
            wzero.append(i)
        else:
            wozero.append(i)
    
    newarr=wzero+wozero
    return(newarr)

A = list(map(int, input().rstrip().split()))
print(move_zeros_to_left(A))
