# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 左右边界
        while left <= right:
            med = (left + right) // 2
            if nums[med] == target:
                return med
            if nums[left] <= nums[med]:
                # 这判断为什么可以得到左边有序呢，因为旋转后
                # 相当于有两个升序数组，且其中一的最小值大于另一个的最大值
                if nums[left] <= target < nums[med]:
                    right = med - 1
                else:
                    left = med + 1
            else:
                if nums[med] < target <= nums[right]:
                    left = med + 1
                else:
                    right = med - 1
        return -1
