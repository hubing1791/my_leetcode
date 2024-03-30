# https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
# 2022-05-07
from typing import List


class Solution:
	def constructArr(self, a: List[int]) -> List[int]:
		# 分别迭代计算
		result = [1] * len(a)
		tmp = 1
		for i in range(len(a) - 1):
			tmp *= a[i]
			result[i + 1] *= tmp
		tmp = 1
		for i in range(-1, -len(a), -1):
			tmp *= a[i]
			result[i-1] *= tmp
		return result
