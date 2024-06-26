# https://leetcode-cn.com/problems/unique-binary-search-trees/


class Solution:
	# 公式法天秀，但是写下迭代法比较靠谱
	def numTrees(self, n: int) -> int:
		dp = [0] * (n + 1)
		dp[0], dp[1] = 1, 1
		for i in range(2, n + 1):
			for j in range(0, i):
				dp[i] += dp[j] * dp[i - j - 1]
		return dp[n]