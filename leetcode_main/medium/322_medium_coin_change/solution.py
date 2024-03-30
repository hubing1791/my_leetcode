# https://leetcode-cn.com/problems/coin-change/
from typing import List


class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		# 参数分别为新的起始位置余额和已使用硬币数，结果列表
		# 思路为优先取大数
		# 逻辑对，栈深度时间遇到特殊的还是爆炸,在我自己电脑上可以跑通
		def helper(index, amount_left, amount_coin, result: List):
			# 这个剪枝方法不够好
			# if result and amount_coin >= min(result):
			#	 return 0
			if result_ and amount_coin+(amount_left//coins[index])>=min(result_):
				return 0
			for i in range(index, k):
				if amount_left > coins[i]:
					helper(i, amount_left - coins[i], amount_coin + 1, result)
				elif amount_left == coins[i]:
					result.append(amount_coin + 1)
				else:
					pass

		if not amount:
			return 0
		else:
			result_ = []
			coins.sort(reverse=True)
			k = len(coins)
			helper(0, amount, 0, result_)
			if not result_:
				return -1
			else:
				# 犯了个无聊的错误，一开始一直返回result_[0]
				return min(result_)


if __name__ == '__main__':
	test_set = [[[1, 2, 5], 11, 3],
				[[2], 3, -1],
				[[1], 0, 0],
				[[1], 2, 2],
				[[3, 7, 405, 436], 8839, 123],
				[[186, 419, 83, 408], 6249, 20],
				[[288, 160, 10, 249, 40, 77, 314, 429], 9208, 123]
				]
	sol = Solution()
	for x, y, z in test_set[6:]:
		print(str(sol.coinChange(x, y)) + '\t' + str(z) + '\n')
