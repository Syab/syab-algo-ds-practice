#!/bin/python3

from hashlib import new
import math
import os
import random
import re
import sys
import collections
from tkinter import N
from types import new_class

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.Head=None

    def printList(self):
        current = self.Head
        while current is not None:
            print(current.data, end=" ")
            current=current.next
        
    def insertIntoEmptyList(self, element):
        newNode = Node(element)
        self.Head = newNode
    
    def insertAtBeginning(self, element):
        if self.Head is None:
            newNode = Node(element)
            self.Head = newNode
        else:
            newNode = Node(element)
            newNode.next = self.Head
            self.Head = newNode
    
    def insertAtEnd(self, element):
        if self.Head is None:
            newNode = Node(element)
            self.Head = newNode
        else:
            current = self.Head
            while current.next is not None:
                current = current.next
            newNode = Node(element)
            current.next = newNode

myLinkedList = LinkedList()
myLinkedList.insertAtBeginning(224)
myLinkedList.insertAtBeginning(12)
myLinkedList.printList()
print("\n")
myLinkedList.insertAtBeginning(45)
myLinkedList.printList()
print("\n")
