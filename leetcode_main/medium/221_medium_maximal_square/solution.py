# https://leetcode-cn.com/problems/maximal-square/

from typing import List


class Solution:
	# 用动态规划求最大边长
	def maximalSquare(self, matrix: List[List[str]]) -> int:
		if not matrix or not matrix[0]:
			return 0
		max_side = 0
		width, length = len(matrix), len(matrix[0])
		dp = [[0] * length for i in range(width)]
		for i in range(width):
			for j in range(length):
				# 里面是字符串不是数字
				if matrix[i][j] == '1':
					# 在边上则按数字赋值即可
					if i == 0 or j == 0:
						dp[i][j] = 1
					else:
						# 由格子所在2x2小方块其它几个格子决定
						dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
				max_side = max(max_side, dp[i][j])
		return max_side * max_side


if __name__ == '__main__':
	test_set = [
		[[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]],
		 4]
	]
	sol = Solution()
	for x,y in test_set:
		print(str(sol.maximalSquare(x))+'\t'+str(y))
