#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    tarr=s.split(":")
    thour=tarr[0]
    if (tarr[2][2:] == 'PM'):
        if (thour<12):
            thour = int(thour) + 12
            print(str(thour)+":"+tarr[1]+":"+tarr[2][:2])
        else:
            print(str(thour)+":"+tarr[1]+":"+tarr[2][:2])
    else:
        if (int(thour) == 12):
            print("00:"+tarr[1]+":"+tarr[2][:2])
        else:    
            print(tarr[0]+":"+tarr[1]+":"+tarr[2][:2])


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    # fptr.write(result + '\n')
    # fptr.close()