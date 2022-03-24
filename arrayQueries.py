#!/bin/python3

import math
import os
import random
import re
import sys
import collections
import itertools

def solveOne(ar, Q, inputar):
    r1=Q[1]
    r2=Q[2]
    addVal=Q[3]
    count=0
    for elem in range(r1-1, r2):
        ar[elem] = ar[elem] + addVal
    # print (ar)
    return (ar,count)

# WRONG SOLUTION
def solveTwo(ar, Q, inputar):
    most_occurred_count = 0
    count = 0
    remainder = 0
    remlist = []
    r1=Q[1]
    r2=Q[2]
    divisor=inputar[1]
    for elem in range(r1-1, r2):
        remainder=ar[elem]%divisor
        # print (remainder)
        remlist.append(remainder)
    
    # print(remlist)
    occurence_count = collections.Counter(remlist)
    most_occurred_count = occurence_count.most_common(1)[0][1]
    print(occurence_count)
    count = int(inputar[0]) - int(most_occurred_count)
    return (ar,count)

def solve(startar,quer,inputar):
    val = 0
    if (quer[0]==1):
        solveOne(startar, quer, inputar)
        startar = startar
    elif (quer[0]==2):
        result=solveTwo(startar, quer, inputar)
        startar= result[0]
        val=result[1]
    return (startar, val)

inputar = input().split()
inputar = list(map(int, inputar))
if (len(inputar) != 3):
    print("Expected number of space separated inputs is 3.")
    exit()
    
N, K, Q = inputar[0],inputar[1],inputar[2] 

ar = input().split()
ar = list(map(int, ar)) 
if (len(ar) != N):
    print("Length of array does not meet specified array length, N")
    exit()

listOfQuer = []
for i in range(Q):
    queryar = input().split()
    queryar = list(map(int,queryar))
    if (len(queryar)==3 or len(queryar)==4):
        listOfQuer.append(queryar)
        # print (listOfQuer)
    else:
        print ("Queries do not meet minimum length")
        exit()

for j in listOfQuer:
    output_= 0
    startar= ar
    output_ = solve(startar,j,inputar)
    if ( j[0] == 2):
        print(output_[1])