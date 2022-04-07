#!/bin/python3

from inspect import stack
import math
import os
import random
import re
import sys
import time

def balancedbrkts(str):

    arr=[]
    # arr.append(-1)

    for i in list(str):
        if (i in ['(', '{','[']):
            arr.append(i)
            print(arr)
        else:
            if not arr:
                return False
            current_char = arr.pop()
            print(current_char)
            if current_char == '(':
                if (i != ')'):
                    return False
            if current_char == '[':
                if (i != ']'):
                    return False
            if current_char == '{':
                if (i != '}'):
                    return False
    if arr:
        return False
    return True


str=input()
if (balancedbrkts(str)):
    print ("Balanced")
else:
    print("Not Balanced")