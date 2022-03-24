#!/bin/python3

from hashlib import new
import math
import os
import random
import re
import sys
import time

nemo=['nemo']
larArr = ['nemo']*10000

def findNemo(myarr):
    starttime = time.time()
    for i in myarr:
        if (i == 'nemo'):
            print('Found Nemo!')
        else:
            print('NOT Nemo!')
    endtime= time.time()
    print(endtime-starttime)

findNemo(larArr)

# start = time.time()
# print("hello")
# end = time.time()
# print(end - start)