# https://leetcode-cn.com/problems/next-greater-element-ii/
from typing import List


class Solution:
	# 利用单调栈
	def nextGreaterElements(self, nums: List[int]) -> List[int]:
		stack = []
		length = len(nums)
		result = [-1] * length
		for i in range(length * 2 - 1, -1, -1):
			while stack and nums[i % length] >= nums[stack[-1]]:
				stack.pop()
			result[i % length] = -1 if not stack else nums[stack[-1]]
			stack.append(i % length)
		return result

	# 写一个正向循环的版本
	def nextGreaterElements_1(self, nums: List[int]) -> List[int]:
		stack = []
		length = len(nums)
		result = [-1] * length
		for i in range(length * 2):
			while stack and nums[stack[-1] % length] < nums[i % length]:
				result[stack.pop() % length] = nums[i % length]
			stack.append(i % length)
		return result


if __name__ == "__main__":
	test_set = [
		[1, 2, 1]
	]
	sol = Solution()
	for i in test_set:
		print(sol.nextGreaterElements_1(i))
