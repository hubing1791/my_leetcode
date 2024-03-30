# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/

import math


class Solution:
	def cuttingRope(self, n: int) -> int:
		if n <= 3:
			return n - 1
		a, b = divmod(n, 3)
		if b == 1:
			return int(math.pow(3, a - 1) * 4)
		elif b == 2:
			return int(math.pow(3, a) * 2)
		else:
			return int(math.pow(3, a))
