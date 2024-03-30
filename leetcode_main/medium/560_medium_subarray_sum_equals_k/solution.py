# https://leetcode-cn.com/problems/subarray-sum-equals-k/
from typing import List
from collections import defaultdict


class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		nums_count_dict = defaultdict(int)  # 前缀和计数数组
		nums_count_dict[0] = 1
		pre_sum = 0  # 前缀和
		result = 0
		for i in range(len(nums)):
			pre_sum += nums[i]
			if pre_sum - k in nums_count_dict:
				result += nums_count_dict[pre_sum - k]
			nums_count_dict[pre_sum] += 1
		return result
