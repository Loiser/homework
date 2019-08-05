# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:07:51 2019

@author: 10539
"""

'''三数之和'''
class Solution:
    def threeSum(self,nums):
        nums.sort()
        for i in range(0,len(nums)-3):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    print(nums[i],nums[j],nums[k])
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
if __name__ == "__main__":
    s1=Solution()
    num=[-1,0,1,2,-1]
    s1.threeSum(num)
            