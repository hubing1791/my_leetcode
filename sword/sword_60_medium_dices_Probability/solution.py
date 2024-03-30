# https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/
# 2022-05-06
from typing import List


# 对应题解，用当前得概率列表计算下一轮概率列表
class Solution:
	def dicesProbability(self, n: int) -> List[float]:
		prob = [1.0 / 6.0] * 6

		for i in range(1, n):
			tmp_prob = [0] * (5 * i + 6)
			for j in range(0,len(prob)):
				for k in range(6):
					tmp_prob[j+k] +=prob[j]/6.0
			prob = tmp_prob
		return prob