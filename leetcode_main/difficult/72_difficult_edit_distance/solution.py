# https://leetcode-cn.com/problems/edit-distance/
# 直接看的题解 https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode-solution/
class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		length1 = len(word1)
		length2 = len(word2)
		# 这样的动态规划，第一个数字对应word2的字母位置
		dp = [[0] * (length1 + 1) for i in range(length2 + 1)]
		# 两个边初始化为字符串长度值，因为两个边表示的是空串到某个串的编辑距离
		# 一定等于不空的串长
		for i in range(1, length2 + 1):
			dp[i][0] = i
		for i in range(1, length1 + 1):
			dp[0][i] = i
		for i in range(1, length2 + 1):
			for j in range(1, length1 + 1):
				a,b=word1[j - 1],word2[i - 1]
				if word1[j - 1] == word2[i - 1]:
					dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
				else:
					dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
		return dp[-1][-1]

if __name__ == '__main__':
	test_set = [
		[["horse","ros"],3],
		[["intention","execution"],5]
	]
	sol = Solution()
	for x, y in test_set[0:1]:
		x1,x2 = x
		print(sol.minDistance(x1,x2))
