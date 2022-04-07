#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    c = 0
    bribes = 0
    for i in range(len(q), 0, -1):
        for j in range(len(q)-1, -1, -1):
            if q[j] != i:
                c +=1
                if c > 2:
                    print("Too Chaotic")
                    return
            else:
                bribes += c
                c = 0
                q.pop(j)
                break
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
