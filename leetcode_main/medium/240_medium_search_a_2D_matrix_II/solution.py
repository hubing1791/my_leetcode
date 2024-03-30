# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
from typing import List


class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		width, length = len(matrix), len(matrix[0])
		# 从右上角开始找
		x, y = 0, length - 1
		while x < width and y >= 0:
			if matrix[x][y] < target:
				x += 1
			elif matrix[x][y] > target:
				y -= 1
			else:
				return True
		return False


if __name__ == "__main__":
	test_set = [
		[[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
		 5]
	]
	sol = Solution()
	for x1, x2 in test_set:
		print(sol.searchMatrix(x1, x2))
