#!/bin/python3

import math
import os
import random
import re
import sys
import collections


s = "race a car"

def isPalindrome(s):
    # s = ''.join(filter(str.isalnum, s)).lower()
    # s = s.lower()
    s = ''.join(i for i in s if i.isalnum()).lower()
    print(s)
    if s == s[::-1]:
        print("IS PALINDROME")
    else:
        print("IS NOT")

isPalindrome(s)
