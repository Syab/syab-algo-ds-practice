#!/bin/python3

import math
import os
import random
import re
import sys


'''
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''
nums = [1,2,3,1]

def containsDuplicate(nums):
    hashmap={}
    for i in nums:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    for j in hashmap:
        if hashmap[j] > 1:
            print("CONTAINS DUPLICATE")
            break
  
containsDuplicate(nums)