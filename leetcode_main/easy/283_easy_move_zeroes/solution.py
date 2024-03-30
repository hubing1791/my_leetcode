# https://leetcode-cn.com/problems/move-zeroes/

from typing import List


class Solution:
	# 自己写的判断条件太多实在太慢了
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		left, right = 0, 0
		while right < len(nums):
			while left<len(nums) and nums[left]:
				left += 1
			right = left
			while right<len(nums) and not nums[right] :
				right += 1
			if left<len(nums) and right<len(nums):
				nums[left], nums[right] = nums[right], nums[left]
			right+=1
