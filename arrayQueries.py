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
    # INCOMPLETE ############
    return

def solveTwo(ar, Q, inputar):
    return

def solve(startar,quer,inputar):
    val = 0
    if (quer[0]==1):
        solveOne(startar, quer, inputar)
    elif (quer[0]==2):
        solveTwo(startar, quer, inputar)
    return (startar, val)

inputar = input().split()
inputar = list(map(int, inputar))
if (len(inputar) != 3):
    print("Expected number of space separated inputs is 3.")
    exit()
N = inputar[0]
K = inputar[1]
Q = inputar[2]

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
        print (listOfQuer)
    else:
        print ("Queries do not meet minimum length")
        exit()

for j in listOfQuer:
    output_= 0
    startar= ar
    output_ = solve(startar,j,inputar)
    print(output_)

# output_ = solve(ar, N)
# print (output_)