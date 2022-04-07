#!/bin/python3

import math
import os
import random
import re
import sys
import collections

def revInplace(arr):
    lo, hi = 0, len(arr)-1
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo +=1
        hi -= 1
        print(arr)

arr=list(input())
revInplace(arr)
