#!/bin/python3

from hashlib import new
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

class SinglyLinkedList:
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
    
    def insertAtPosition(self, element, position):
        counter = 1
        current = self.Head
        while counter < position -1 and current is not None:
            counter +=1
            current = current.next
        if position == 1 :
            newNode = Node(element)
            newNode.next = current
            self.Head = newNode
        else:
            newNode=Node(element)
            newNode.next = current.next
            current.next = newNode

def insertNodeAtPosition(llist, data, position):
    llist = SinglyLinkedList()
    llist.insertAtPosition(data, position)
    # llist.printList()
    # print("\n")

llist_count = int(input())
llist = SinglyLinkedList()
for _ in range(llist_count):
    llist_item = int(input())
    llist.insertAtEnd(llist_item)

# data = int(input())
# position =int(input())

insertNodeAtPosition(llist, 3, 1)
# llist_head = insertNodeAtPosition(llist, data, position)
llist.printList()
print("\n")