#!/bin/python3

from hashlib import new
import math
import os
import random
import re
import sys
import time

"""
[MEDIUM LEVEL]
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""
