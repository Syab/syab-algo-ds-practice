#!/bin/python3

from ctypes.wintypes import tagRECT
import math
from operator import ne
import os
import random
import re
import sys
import collections

def twosum(nums, target):
    newSet = set(nums)
    ans = []
    for i in range(len(nums)):
        val = target - nums[i]
        if val in newSet:
            position = nums.index(val)
            ans.append(position)
        # else:
        #     print("NOT IN SET")
    # list(set(ans))
    return(list(set(ans)))

def weikai(nums, target):
    track = {}
    res = []
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement not in track.keys():
            track[complement] = i
            # print(track)
        else:
            res.append([i, track[complement]])
            print(i)
    return res

def correctsol(nums, target):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_ind = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in val_to_ind:
                return [i, val_to_ind[diff]]
            
            val_to_ind[num] = i

target= int(input())
nums = list(map(int, input().rstrip().split()))
# print(weikai(nums, target))
print(twosum(nums, target))