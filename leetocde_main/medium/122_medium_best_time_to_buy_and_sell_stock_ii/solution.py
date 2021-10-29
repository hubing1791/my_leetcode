# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
# 2021-10-01

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        price_prev = prices[0]
        for price in prices[1:]:
            if price > price_prev:
                result += price - price_prev
            price_prev = price
        return result