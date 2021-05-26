# https://leetcode-cn.com/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        dfs_list = [0] * length
        dfs_list[0] = nums[0]
        dfs_list[1] = max(nums[0], nums[1])
        for i in range(2, length):
            dfs_list[i] = max(dfs_list[i - 1], dfs_list[i - 2] + nums[i])
        return dfs_list[-1]
