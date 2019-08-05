# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:25:02 2019

@author: 10539
"""
'''array'''
def mergelist(l1,l2):
    l1[len(l1):len(l1)+len(l2)]=l2
    return l1.sort()
'''singlelist''' 
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None      
class singlelist:
    def __init__(self,node=None):
        self._head=node
    def is_empty(self):
        return self._head==None       
    def insert(self,pos,elem):
        node=Node(elem)
        if pos<0:
            print("errro")
            return False
        else:
            index=0
            pre=self._head
            while index <(pos-1) and pre!=None:
                pre=pre.next
                index+=1
            node.next=pre.next
            pre.next=node
    def remove(self,elem):
        curr=self._head
        pre=None
        while curr!=None:
            if curr.val==elem:
                if curr==self._head:
                    self._head=curr.next
                else:
                    pre.next=curr.next
                break
            else:
                pre=curr
                curr=curr.next
    def index(self,pos):
        if pos<0:
            print("errro")
            return False
        else:
            index=1
            curr=self._head
            while index <(pos):
                if curr.next!=None:
                    curr=curr.next
                    index+=1
                else:
                    print("over range")
                    return False
        return curr.val
    def inverse(self):
        wareh=list()
        pre=self._head
        while pre!=None:
            wareh.append(pre)
            pre=pre.next
        wareh.reverse()
        i=1
        while i<len(wareh):
            now=wareh(i)
            now.next=wareh(i+1)
        self._head=wareh(1)
        
'''combine up以单向链表为例,
循环列表记录head作为停止循环条件'''
def merge(l1,l2):
    res=singlelist()
    pre=res._head
    if l1 is None:
        res._head=l2._head
    if l2 is None:
        res._head=l1._head
    curl1=l1._head
    curl2=l2._head
    if curl1.val<curl2.val:
        pre=curl1
        curl1=curl1.next
    else:
        pre=curl2
        curl2=curl2.next
    while curl1!=None and curl2!=None:
        if curl1.val<curl2.val:
            pre.next=curl1
            curl1=curl1.next
        else:
            pre.next=curl2
            curl2=curl2.next
'''circle'''     
class circlelist:
    def __init__(self,node=None):
        self._head=node
        if node:
            node.next=node
    def is_empty(self):
        return self._head==None       
    def insert(self,pos,elem):
        node=Node(elem)
        if pos<0:
            print("errro")
            return False
        else:
            index=0
            pre=self._head
            while index <(pos-1):
                pre=pre.next
                index+=1
            node.next=pre.next
            pre.next=node
    def remove(self,elem):
        if self.is_empty():
            return
        curr=self._head
        pre=None
        while curr.next!=self._head:
            if curr.val==elem:
                if curr==self._head:
                    rear=self._head
                    while rear.next!=self._head:
                        rear=rear.next
                    self._head=curr.next
                    rear.next=self._head
                else:
                    pre.next=curr.next
                return
            else:
                pre=curr
                curr=curr.next
        if curr.val==elem:
            if curr==self._head:
                self._head=None
            else:
                pre.next=curr.next
    def index(self,pos):
        if pos<0:
            print("errro")
            return False
        else:
            index=1
            curr=self._head
            while index <(pos):
                if curr.next!=self._head:
                    curr=curr.next
                    index+=1
                else:
                    print("over range")
                    return False
        return curr.val      

                     
        
            
    
    
