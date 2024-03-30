# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/

from typing import List


class Solution:
	# 两次使用单调栈，和接雨水异曲同工
	# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode-/
	def largestRectangleArea(self, heights: List[int]) -> int:
		n = len(heights)
		left, right = [0] * n, [0] * n
		mono_stack = []
		for i in range(n):
			while mono_stack and heights[mono_stack[-1]] >= heights[i]:
				mono_stack.pop()
			left[i] = mono_stack[-1] if mono_stack else -1
			mono_stack.append(i)
		mono_stack = []
		for i in range(n - 1, -1, -1):
			while mono_stack and heights[mono_stack[-1]] >= heights[i]:
				mono_stack.pop()
			right[i] = mono_stack[-1] if mono_stack else n
			mono_stack.append(i)
		ans = 0
		for i in range(n):
			ans = max((right[i] - left[i] - 1) * heights[i], ans)
		return ans

	# 优化版，也是看的答案
	def largestRectangleArea(self, heights: List[int]) -> int:
		n = len(heights)
		# 注意right要初始化为n
		left, right = [0] * n, [n] * n
		mono_stack = []
		for i in range(n):
			while mono_stack and heights[mono_stack[-1]] >= heights[i]:
				right[mono_stack[-1]] = i
				mono_stack.pop()
			left[i] = mono_stack[-1] if mono_stack else -1
			mono_stack.append(i)
		ans = 0
		for i in range(n):
			ans = max((right[i] - left[i] - 1) * heights[i], ans)
		return ans
