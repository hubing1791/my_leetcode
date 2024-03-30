# https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
# 2022-05-03
from typing import List


class Solution:
	# 方法正确，但是会超时
	def maxValue(self, grid: List[List[int]]) -> int:
		if not grid or not grid[0]:
			return 0
		result = 0
		x_border, y_border = len(grid) - 1, len(grid[0]) - 1

		def move(sum_value: int, x: int, y: int):
			nonlocal result
			if x == x_border and y == y_border:
				sum_value += grid[x][y]
				result = max(result, sum_value)
				return
			else:
				sum_value += grid[x][y]
				for move_x, move_y in [[0, 1], [1, 0]]:
					x_new = x + move_x
					y_new = y + move_y
					if x_new <= x_border and y_new <= y_border:
						move(sum_value, x_new, y_new)

		move(0, 0, 0)
		return result

	def maxValue_DP(self, grid: List[List[int]]) -> int:
		result = 0
		x_border, y_border = len(grid), len(grid[0])
		dp_martix = [[0] * (y_border + 1) for _ in range(x_border + 1)]
		for i in range(1, x_border + 1):
			for j in range(1, y_border + 1):
				dp_martix[i][j] = max(dp_martix[i - 1][j], dp_martix[i][j - 1]) + grid[i - 1][j - 1]
		return dp_martix[-1][-1]


if __name__ == '__main__':
	so = Solution()
	test_set = [
		[[1, 3, 1], [1, 5, 1], [4, 2, 1]],
		[[7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5], [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
		 [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8], [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
		 [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4], [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
		 [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4], [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
		 [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3], [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
		 [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7], [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9]]
	]
	print(so.maxValue(test_set[1]))
