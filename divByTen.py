#!/bin/python3

import itertools

def findPerfectTen(mulpdt):
    count = 0
    for i in mulpdt:
        if (i%10 == 0):
            count += 1
        else:
            count = count
    return count

def mutiplyTuples(products):
    mulpdt = []
    for i in products:
        temp = i[0]*i[1]
        mulpdt.append(temp)
    return mulpdt

def solve(ar,N):
    print(ar)
    products = []
    for i in itertools.combinations(ar,2):
        products.append(i)
    
    print (products)
    mulpdt=mutiplyTuples(products)
    countDivByTen= findPerfectTen(mulpdt)
    return countDivByTen

N = int(input())
ar = input().split()
ar = list(map(int, ar)) 

output_ = solve(ar, N)
print (output_)