# https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
# 2022-05-06
from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		result = 0
		if not prices:
			return result
		min_p = prices[0]
		for x in prices:
			if x < min_p:
				min_p = x
			if x > min_p:
				result = max((x - min_p), result)
		return result
