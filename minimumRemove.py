#!/bin/python3

import math
import os
import random
import re
import sys
import collections
import itertools


def getGcd(ar):
    gcd_ = 0
    gcdis = math.gcd(*ar)
    if ( gcdis == 1):
        print (ar)
    else:
        print (gcdis)
        gcd_ = gcdis
    return gcd_
    

def solve(N, ar):
    gcd=getGcd(ar)
    return gcd

T = int(input())
for _ in range(T):
    N = int(input())
    ar = input().split()
    ar = list(map(int, ar)) 
    output_ = solve(N, ar)

    # for i in range(0, N):
    #     ar = []
    #     ar.append(int(input()))
    #     print (ar)
    #     out_ = solve(ar)
    #     print(out_)

