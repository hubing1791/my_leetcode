# https://leetcode-cn.com/problems/min-stack/

import sys


class MinStack:

	def __init__(self):
		self.stack = []
		self.min_stack = [sys.maxsize]

	def push(self, x: int) -> None:
		self.stack.append(x)
		self.min_stack.append(min(x, self.min_stack[-1]))

	def pop(self) -> None:
		self.stack.pop()
		self.min_stack.pop()

	def top(self) -> int:
		return self.stack[-1]

	def getMin(self) -> int:
		return self.min_stack[-1]



if __name__ == "__main__":
	if not []:
		print('hhhh')
	# minstack = MinStack()
	# list = [-2, 0, -3]
	# for i in list:
	#	 minstack.push(i)
	# print(minstack.getMin())
	# minstack.pop()
	# print(minstack.top())
	# print(minstack.getMin())
