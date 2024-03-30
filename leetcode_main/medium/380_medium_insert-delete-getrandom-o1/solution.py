# https://leetcode.cn/problems/insert-delete-getrandom-o1
# 2024-03-29

from collections import deque
from random import choice

class RandomizedSet:

	def __init__(self):
		self._dict = {}
		self._list = deque()


	def insert(self, val: int) -> bool:
		if val in self._dict:
			return False
		self._dict[val] = len(self._list)
		self._list.append(val)
		return True

	def remove(self, val: int) -> bool:
		if val in self._dict:
			index = self._dict[val]
			self._list[index]=self._list[-1]
			self._dict[self._list[-1]] = index
			self._dict.pop(val)
			self._list.pop()
			return True
		return False


	def getRandom(self) -> int:
		return choice(self._list)