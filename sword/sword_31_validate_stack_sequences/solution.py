# https://leetcode-cn.com/problems/validate-stack-sequences/
# 2022-04-27
from typing import List


class Solution:
	def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
		stack = []
		index_pop,length = 0,len(popped)
		for x in pushed:
			stack.append(x)
			if index_pop == length:
				break
			while stack and stack[-1] == popped[index_pop]:
				stack.pop()
				index_pop +=1
		return index_pop == length