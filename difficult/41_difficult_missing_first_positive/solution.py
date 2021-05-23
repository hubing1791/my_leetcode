# https://leetcode-cn.com/problems/first-missing-positive/
from typing import List


class Solution:
    # 官解的第一种方法，哈希表法
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1
        for i in range(length):
            if 0 < abs(nums[i]) <= length:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(length):
            if nums[i] > 0:
                return i + 1
        return length + 1

    # 官方解答第二种
    def firstMissingPositive1(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            while 1 <= nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        for i in range(length):
            if nums[i]!=i+1:
                return i+1
        return length+1
