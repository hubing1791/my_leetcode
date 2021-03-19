# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashmap = set()
        for i in nums:
            if i in hashmap:
                return i
            else:
                hashmap.add(i)
