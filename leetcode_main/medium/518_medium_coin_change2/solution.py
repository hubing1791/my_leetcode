# https://leetcode-cn.com/problems/coin-change-2/

from typing import List


class Solution:
	# 很经典的动态规划，参考了答案
	def change(self, amount: int, coins: List[int]) -> int:
		dp = [0] * (amount + 1)
		dp[0] = 1
		for coin_price in coins:
			for i in range(coin_price, amount + 1):
				dp[i] += dp[i - coin_price]
		return dp[amount]
