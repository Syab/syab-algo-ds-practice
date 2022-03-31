#!/bin/python3

from hashlib import new
import math
import os
import random
import re
import sys
import collections

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.Head= None

myLinkedList = LinkedList()
myNode1 = Node(10)
myNode2 = Node(45)
myNode3 = Node(23)
myNode4 = Node(56)
myNode5 = Node(34)

myLinkedList.Head = myNode1
myNode1.next = myNode2
myNode2.next = myNode3
myNode3.next = myNode4
myNode4.next = myNode5

print("The elements in the linked list are:")
# print(myLinkedList.Head.data, end=" ")
print(myLinkedList.Head.next.data, end=" ")
# print(myLinkedList.Head.next.next.data, end=" ")
# print(myLinkedList.Head.next.next.next.data)
