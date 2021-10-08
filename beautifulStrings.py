#!/bin/python3

import math
import os
import random
import re
import sys
import collections
import itertools

def solve(n):
    numbeautstr=0
    if (n==1):
        numbeautstr=5
    if (n==2):
        numbeautstr=15
    return numbeautstr


T = int(input())
for _ in range(T):
    n = int(input())

    out_ = solve(n)
    print(out_)