# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
	# 一开始忘记对[]处理
	def maxProfit(self, prices: List[int]) -> int:
		profit = 0
		if not prices:
			return profit
		min_history = prices[0]
		for i in range(1, len(prices)):
			if prices[i] < min_history:
				min_history = prices[i]
			else:
				if prices[i] - min_history > profit:
					profit = prices[i] - min_history
		return profit
