from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 题目不要求我们按照顺序返回三元组，因此我们不妨先对数组进行排序，这样就可以方便地跳过重复的元素。
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                """
                如果x<0，则说明nums[j]太小，我们需要将j右移一位
                如果x>0，则说明nums[k]太大，我们需要将k左移一位
                如果找到合法的三元组，则将其加入答案，并将j右移一位，k左移一位
                """
                x = nums[i] + nums[j] + nums[k]
                if x < 0:
                    j += 1
                elif x > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans
    
print(Solution().threeSum([0,0,0]))
print(Solution().threeSum([-1,0,1,2,-1,-4]))