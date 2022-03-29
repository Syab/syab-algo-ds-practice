#!/bin/python3

import math
import os
import random
import re
import sys
import time

def printrev(arr):
    revstck=[]
    for i in arr:
        revstck.insert(0,i)
        
    return(revstck)

arr = input().split(" ")
print(printrev(arr))