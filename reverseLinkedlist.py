#!/bin/python3

import math
import os
import random
import re
import sys
import collections
from tkinter import N
from turtle import position
from types import new_class

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

