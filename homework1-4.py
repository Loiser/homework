# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:32:10 2019

@author: 10539
"""

class Solution:
    def monum(self,nums):
        cal=0
        monu=0
        while len(nums)>cal:
            if nums.count(nums[0])>cal:
                cal=nums.count(nums[0])
                monu=nums[0]
            for nums[0] in nums:
                nums.remove(nums[0])
        print(monu)      
if __name__ == "__main__":
    s1=Solution()
    num=[-1,0,1,2,-1]
    s1.monum(num)

