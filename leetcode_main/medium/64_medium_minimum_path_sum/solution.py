# https://leetcode-cn.com/problems/minimum-path-sum/
from typing import List


class Solution:
	# 比较简单的动态规划
	def minPathSum(self, grid: List[List[int]]) -> int:
		m, n = len(grid), len(grid[0])
		for i in range(m):
			for j in range(n):
				if i and j:
					grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
				elif not i and not j:
					pass
				elif not i:
					grid[i][j] += grid[i][j - 1]
				else:
					grid[i][j] += grid[i - 1][j]
		return grid[-1][-1]
