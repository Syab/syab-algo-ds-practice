#!/bin/python3

import math
import os
import random
import re
import sys
import collections


def countingValleys(steps, path):
    sealevel = 0
    valleys = 0
    for i in path:
        if (i == "U"):
            sealevel += 1
        else:
            sealevel -= 1
        if ( sealevel == 0 and i == "U"):
            valleys += 1
    print(valleys)
    return valleys

steps = int(input().strip())
path = input().upper()

result = countingValleys(steps, path)
