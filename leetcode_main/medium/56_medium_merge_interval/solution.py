# https://leetcode-cn.com/problems/merge-intervals/
from typing import List


class Solution:
	# 思路一下子想到了，还是看了解答，解答的想法更好
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		intervals.sort(key=lambda x: x[0])
		result = []
		for i in intervals:
			if not result or result[-1][1] < i[0]:
				result.append(i)
			else:
				result[-1][1] = max(i[1], result[-1][1])
		return result
