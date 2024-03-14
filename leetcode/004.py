from math import inf
from typing import List

"""

1，确保对输入的数组进行适当处理，使得 nums1 的长度小于等于 nums2 的长度。
这样做的目的是确保在二分查找时，我们总是在较短的数组上进行操作，以保证时间复杂度为 O(log(min(m,n)))。

2，在较短的数组上使用二分查找。在 nums1 上进行二分查找，同时利用总长度的一半 (m+n+1)/2 来分割，
使得左侧部分的长度等于右侧部分的长度或多一个元素。

3，通过二分查找，不断调整左侧和右侧的划分，直到满足以下条件：
    nums1[i-1] <= nums2[j]，其中 i 是 nums1 的分割点左侧的元素数量，j 是 nums2 的分割点左侧的元素数量。
    nums2[j-1] <= nums1[i]，即确保分割点满足左侧元素都小于右侧元素。
    当满足这两个条件时，我们就找到了中位数所在的位置。

4，根据数组长度为奇数或偶数的情况，计算中位数。

"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 的长度小于等于 nums2 的长度
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        total_len = (m + n + 1) // 2
        
        while left < right:
            # 二分查找 nums1 的分割点
            i = left + (right - left) // 2
            j = total_len - i
            
            """
            分割点的两个条件确保了合并后的数组被分成了两个部分，并且左侧部分的所有元素都小于等于右侧部分的所有元素。这样的划分保证了中位数的定义：

            对于奇数个元素的情况，中位数是合并后数组的中间值，即左侧部分的最大值；
            对于偶数个元素的情况，中位数是合并后数组中间两个数的平均值。
            
            这两个条件确保了中位数的定义在合并后的数组中是满足的。
            通过二分查找不断调整分割点的位置，直到找到满足这两个条件的位置，我们就找到了中位数所在的位置。
            """
            # 确保分割点满足条件 nums1[i-1] <= nums2[j] 和 nums2[j-1] <= nums1[i]
            if nums1[i] < nums2[j - 1]:
                left = i + 1
            else:
                right = i

        print(f'left={left} && right={right}')
        
        i = left
        j = total_len - left
        
        print(f'i={i} && j={j}')

        # 计算中位数
        nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right_min = float('inf') if i == m else nums1[i]
        
        nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right_min = float('inf') if j == n else nums2[j]
        
        if (m + n) % 2 == 0:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
        else:
            return max(nums1_left_max, nums2_left_max)

    
# nums1 = [1,3]
# nums2 = [2]

caller=Solution()
# result=caller.findMedianSortedArrays(nums1,nums2)
# print(result)

# nums1 = [1,2]
# nums2 = [3,4]

# result=caller.findMedianSortedArrays(nums1,nums2)
# print(result)


nums1 = [1,2,4,5,6]
nums2 = [3,4,7,8,10,11]
#1,2,3,4,4,5,6,7,8,10,11

result=caller.findMedianSortedArrays(nums1,nums2)
print(result)