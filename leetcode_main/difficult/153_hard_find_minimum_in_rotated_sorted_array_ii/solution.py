# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
# 2022-04-25
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 取最后一个数作为标记
        right, left = len(nums) - 1, 0
        while left < right:
            med = (left + right) // 2
            if nums[med] < nums[right]:
                # 因为整除2的原因，right至少要左移一个
                right = med
            elif nums[med] > nums[right]:
                # 如果left，right只差1，left可能会不移动
                left = med + 1
            else:
                right -= 1
        return nums[left]
