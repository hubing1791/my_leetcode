# https://leetcode-cn.com/problems/single-number/
from typing import List


class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		result = nums[0]
		for i in nums[1:]:
			result = result ^ i
		return result
