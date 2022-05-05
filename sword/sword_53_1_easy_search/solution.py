# https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
# 2022-05-05
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = 0
        for x in nums:
            if x == target:
                result += 1
        return result
