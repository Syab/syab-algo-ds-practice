#!/bin/python3

import math
import os
import py_compile
import random
import re
import sys
import collections

vowels = {'a','e','i','o','u'}

def count_vowels(inpstring):
    vcount = 0
    strarr = list(inpstring)
    print(strarr)
    for char in strarr:
        if char in vowels:
            vcount +=1 
            print(vcount)
    print(vcount)

inpstring = str(input())
count_vowels(inpstring)