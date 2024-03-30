# https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
# 2022_04_27
from typing import List


class Solution:
	def exchange(self, nums: List[int]) -> List[int]:
		index_left, index_right = 0, len(nums) - 1
		while index_left < index_right:
			while index_left<index_right and nums[index_left] % 2 == 1:
				index_left += 1
			while index_left<index_right and nums[index_right] % 2 == 0:
				index_right -= 1
			if index_left < index_right:
				nums[index_left], nums[index_right] = nums[index_right], nums[index_left]
		return nums