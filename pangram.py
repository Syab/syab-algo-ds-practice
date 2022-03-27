#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    strarr=s.split()
    newstr=''.join(strarr).lower()
    setofstr=set(newstr)
    x=re.search("[0-9]",newstr)
    if x:
        return("not pangram")
    else:
        if (len(setofstr) == 26 ):
            return("pangram")
        else:
            return("not pangram")


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    # result = pangrams(s)

    # fptr.write(result + '\n')

    # fptr.close()
    pangrams(s)