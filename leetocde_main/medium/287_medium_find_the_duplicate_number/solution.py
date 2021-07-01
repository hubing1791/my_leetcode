# https://leetcode-cn.com/problems/find-the-duplicate-number/
from typing import List


class Solution:
    # 标记下标法,这个版本不可行，这种只有在抽屉原理的情况下可行
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
    # 标记下标法修改版，因为如果有重复，必然把某个下标改成负的再改回来，就检测到了重复了
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
            else:
                return abs(nums[i])