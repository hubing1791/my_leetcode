# https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/
# 2022-05-06

from collections import deque


# 空间换时间,官方题解第二种
class MaxQueue:

	def __init__(self):
		self.queue = deque()
		self.max_queue = deque()

	def max_value(self) -> int:
		return -1 if not self.max_queue else self.max_queue[0]

	def push_back(self, value: int) -> None:
		self.queue.append(value)
		while self.max_queue and self.max_queue[-1] < value:
			self.max_queue.pop()
		self.max_queue.append(value)

	def pop_front(self) -> int:
		if not self.queue:
			return - 1
		else:
			if self.max_queue[0] == self.queue[0]:
				self.max_queue.popleft()
			return self.queue.popleft()

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
