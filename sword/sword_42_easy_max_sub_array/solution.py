# https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
# 2022-05-01
from typing import List


class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		pre = result = nums[0]
		for x in nums[1:]:
			pre = max(pre + x, x)
			result = max(pre, result)
		return result
