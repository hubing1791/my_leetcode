# https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
# 2022-05-01
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore 投票算法
        cand = nums[0]
        count = 1
        for x in nums[1:]:
            if x == cand:
                count += 1
            else:
                count -= 1
                if count == 0:
                    cand = x
                    count = 1
        return cand
