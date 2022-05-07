# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
# 2022-05-05
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            num_dict[num] = num not in num_dict
        for k,v in num_dict.items():
            if v:
                return k

    def singleNumber_off1(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones