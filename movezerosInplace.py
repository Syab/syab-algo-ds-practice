#!/bin/python3

import math
import os
import random
import re
import sys
import collections
import itertools

def move_zeros_to_left(A):
  if len(A) < 1:
    return

  lengthA = len(A)
  write_index = lengthA - 1
  read_index = lengthA - 1

  while(read_index >= 0):
    print("write",write_index, ":", A[write_index])
    print("read",read_index, ":", A[read_index])
    if A[read_index] != 0:
      A[write_index] = A[read_index]
      write_index -= 1
    read_index -= 1
    print("write aft",write_index, ":", A[write_index])
    print("read aft",read_index, ":", A[read_index])
    

  while(write_index >= 0):
    A[write_index]=0;
    write_index-=1
    
# v = [1, 10, 20, 0, 59, 63, 0, 88, 0]
v = [5, 6, 7 , 0, 3, 0, 4]
print("Original Array:", v)

move_zeros_to_left(v)

print("After Moving Zeroes to Left: ", v)