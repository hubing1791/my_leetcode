class Solution:
	def climbStairs(self, n: int) -> int:
		climb_1 = 1
		climb_2 = 2
		if n <= 2:
			return n
		else:
			i = 3
			while i < n + 1:
				temp = climb_2
				climb_2 = climb_1 + climb_2
				climb_1 = temp
				i += 1
		return climb_2