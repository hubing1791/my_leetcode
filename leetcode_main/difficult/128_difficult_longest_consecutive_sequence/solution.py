# https://leetcode-cn.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		nums_set = set(nums)
		max_seq_num = 0
		for i in range(len(nums)):
			if nums[i] - 1 in nums_set:
				continue
			else:
				temp_num = 1
				while (nums[i] + temp_num) in nums_set:
					temp_num += 1
				max_seq_num = max(max_seq_num, temp_num)
		return max_seq_num
