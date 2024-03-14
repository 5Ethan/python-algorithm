# https://doocs.github.io/leetcode/lc/1.html

from typing import List

class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        m={}
        for i,x in enumerate(nums):
            y=target-x
            if y in m:
                return [m[y],i]
            m[x]=i

caller=Solution()
    
nums = [2,7,11,15]
target = 9
print(caller.twoSum(nums,target))
assert caller.twoSum(nums,target) == [0,1]

nums = [3,2,4]
target = 6
print(caller.twoSum(nums,target))
assert caller.twoSum(nums,target) == [1,2]