# https://leetcode-cn.com/problems/find-peak-element/
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        # 这题和右边比不会越界
        while right > left:
            mid = (right + left) // 2
            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return right
