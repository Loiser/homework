# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:57:23 2019

@author: 10539
"""

class Solution(object):
    def hasCycle(self,head):
        slow=head
        if head==None:
            return False
        fast=head.next
        while slow!=fast:
            if fast==None or fast.next==None:
                return False
            else:
                slow=slow.next
                fast=fast.next.next
        return True