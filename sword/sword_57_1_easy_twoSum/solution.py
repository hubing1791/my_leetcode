# https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
# 2022-05-05
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_set = set()
        for num in nums:
            if target - num in target_set:
                return [num, target - num]
            else:
                target_set.add(num)

    # 双指针法
    def twoSum_two_pointer(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [nums[left], nums[right]]
        return []
