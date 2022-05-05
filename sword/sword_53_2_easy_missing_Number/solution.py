# https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
# 2022-05-05
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums[0] != 0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i] + 1:
                return i + 1
        return len(nums)

    # 因为是排序的，所以下标应该等于值。第一个不符合的即可返回
    def missingNumber1(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

    # 二分查找
    def missingNumber2(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # 这儿的等号十分关键，没有等号，则对于顺序全对的[0]无法解决
        while left <= right:
            med = (left + right) // 2
            # 这种情况表示med左边就已经乱了
            if nums[med] != med:
                right = med - 1
            else:
                left = med + 1
        return left
