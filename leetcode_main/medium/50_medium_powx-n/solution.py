# https://leetcode-cn.com/problems/powx-n/
# 2021-09-09

class Solution:
	def myPow(self, x: float, n: int) -> float:
		def myPowHepler(m: int):
			if m == 0:
				return 1.0
			else:
				y = myPowHepler(m // 2)
				if m % 2 == 1:
					return y * y * x
				else:
					return y * y

		return myPowHepler(n) if n >= 0 else 1 / myPowHepler(-n)

	def myPowIter(self, x: float, n: int):
		result = 1.0
		m = -n if n < 0 else n
		while m:
			if m % 2 == 1:
				result *= x
			# 这一步写的不对，相当于不停看某个位数为不为1，为1乘以对应的次方
			x *= x
			m = m // 2
		return result if n >= 0 else 1 / result
