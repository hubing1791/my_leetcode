# https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/

class Solution:
	# 幂的快速算法，看的解答
	def myPow(self, x: float, n: int) -> float:
		if x == 0:
			return 0
		if n < 0:
			flag = 0
			n = -n
		else:
			flag = 1
		result = 1
		while n:
			if n & 1 == 1:
				result *= x
			n >>= 1
			x *= x
		return result if flag else 1/result
