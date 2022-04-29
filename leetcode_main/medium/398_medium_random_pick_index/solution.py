from collections import defaultdict
from random import randint
from typing import List


# https://leetcode-cn.com/problems/random-pick-index/
# 2022-04-25
class Solution:

    def __init__(self, nums: List[int]):
        self.loc_dict = defaultdict(list)
        for i in range(len(nums)):
            self.loc_dict[nums[i]].append(i)

    def pick(self, target: int) -> int:
        length = len(self.loc_dict[target]) - 1
        return self.loc_dict[target][randint(0, length)]


class Solution1:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = 0
        count = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if randint(0, count) == 0:
                    ans = i
        return ans
