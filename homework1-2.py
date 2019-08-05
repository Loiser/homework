# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:16:45 2019

@author: 10539
"""
class Node(object):
     def __init__(self,item):
         self.elem = item
         self.prev = None
         self.next = None
 
 
class DoubleLinkList(object):
     def __init__(self,node=None):
         self.__head = node
 
     def is_empty(self):
         return self.__head == None
 
     def length(self):
         cur = self.__head
         count = 0
         while cur != None:
             count += 1
             cur = cur.next
         return count
 
     def travel(self):
         cur = self.__head
         while cur != None:
             print(cur.elem,end=" ")
             cur = cur.next
         print("")
 
     def add(self,item):
         node = Node(item)
         cur = self.__head
         node.next = cur
         self.__head = node
 
     def append(self,item):
         node = Node(item)
         cur = self.__head
         prev = None
         if cur == None:
             self.add(item)
         else:
             while cur != None:
                 if cur.next == None:
                     cur.next = node
                     node.prev = cur
                     node.next = None
                     break
                 else:
                     prev = cur
                     cur = cur.next
 
     def insert(self,pos, item):
         node = Node(item)
         cur = self.__head
         prev = None
         count = 0
         if pos <= 0:
             self.add(item)
         elif pos > (self.length()-1):
             self.append(item)
         else:
             while count < pos:
                 if (count+1) == pos:
                     prev.next = node 
                     node.next = cur
                     break
                 else:
                     prev = cur
                     cur = cur.next
                     count += 1
 
 
     def remove(self,item):
         cur = self.__head
         prev = None
         while cur != None:
             if cur.elem == item:
                 if cur == self.__head:
                     self.__head = cur.next
                 else:
                     prev.next = cur.next
                     cur.prev = prev
                 break
             else:
                 prev = cur
                 cur = cur.next
 
     def index(self,pos):
         cur = self.__head
         count = 0
         if pos <= 0 or pos > self.length():
             return False
         else:
             while count < pos:
                 if (count+1) == pos:
                     return cur.elem
                     break
                 else:
                     cur = cur.next
                     count += 1
 
             
 

