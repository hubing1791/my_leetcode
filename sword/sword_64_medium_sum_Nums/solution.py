# https://leetcode-cn.com/problems/qiu-12n-lcof/
# 2022-05-06

class Solution:
	def __init__(self):
		self.res = 0

	def sumNums(self, n: int) -> int:
		n > 0 and self.sumNums(n - 1)
		self.res += n
		return self.res
