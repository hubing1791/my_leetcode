# https://leetcode-cn.com/problems/sort-colors/
from typing import List


class Solution:
	# https://leetcode-cn.com/problems/sort-colors/solution/yan-se-fen-lei-by-leetcode-solution/
	# 答案的方法一,先把0换到前面再把一换到前面
	def sortColors_singlepointer(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		replace_pointer = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				nums[replace_pointer], nums[i] = nums[i], nums[replace_pointer]
				replace_pointer += 1
		for i in range(replace_pointer, len(nums)):
			if nums[i] == 1:
				nums[replace_pointer], nums[i] = nums[i], nums[replace_pointer]
				replace_pointer += 1

	# 答案的方法2，同时换0和1，使用双指针
	def sortColors_2pointer1(self, nums: List[int]) -> None:
		pointer1 = 0
		pointer0 = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				if pointer1 > pointer0:
					# 这步的几个数字的使用顺序很重要，下面注释的这个遇到[0,1]就会出错
					# nums[pointer1], nums[pointer0], nums[i] = nums[pointer0], nums[i], nums[pointer1]
					nums[i], nums[pointer1], nums[pointer0] = nums[pointer1], nums[pointer0], nums[i]
				else:
					nums[i], nums[pointer0] = nums[pointer0], nums[i]
				pointer0 += 1
				pointer1 += 1
			elif nums[i] == 1:
				nums[i], nums[pointer1] = nums[pointer1], nums[i]
				pointer1 += 1

	# 双指针一个从前向后一个从后向前，这个方法快得多
	def sortColors_2pointer2(self, nums: List[int]) -> None:
		n = len(nums)
		pointer0 = 0
		pointer2 = n - 1
		i = 0
		while i <= pointer2:
			while i <= pointer2 and nums[i] == 2:
				nums[i], nums[pointer2] = nums[pointer2], nums[i]
				pointer2 -= 1
			if nums[i] == 0:
				nums[i], nums[pointer0] = nums[pointer0], nums[i]
				pointer0 += 1
			i += 1

