# https://leetcode-cn.com/problems/sort-of-stacks-lcci/

class SortedStack:

	def __init__(self):
		self.sorted_stack = []

	def push(self, val: int) -> None:
		if not self.sorted_stack:
			self.sorted_stack.append(val)
		else:
			if val < self.sorted_stack[-1]:
				self.sorted_stack.append(val)
			else:
				temp_stack = []
				while self.sorted_stack and self.sorted_stack[-1] < val:
					temp_stack.append(self.sorted_stack.pop())
				self.sorted_stack.append(val)
				while temp_stack:
					self.sorted_stack.append(temp_stack.pop())

	def pop(self) -> None:
		if not self.sorted_stack:
			pass
		else:
			self.sorted_stack.pop()

	def peek(self) -> int:
		if not self.sorted_stack:
			return -1
		else:
			return self.sorted_stack[-1]

	def isEmpty(self) -> bool:
		if not self.sorted_stack:
			return True
		else:
			return False
