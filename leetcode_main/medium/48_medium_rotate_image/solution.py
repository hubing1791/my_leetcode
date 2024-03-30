# https://leetcode-cn.com/problems/rotate-image/
from typing import List


class Solution:
	# (x,y)->(y,n-1-x),这个是旋转公式
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		# 一个点按照规律旋转4次即可
		n = len(matrix)
		for x in range(n // 2):
			for y in range(x, n - x - 1):
				x1, y1 = x, y
				temp_num = matrix[x1][y1]
				for i in range(4):
					temp_num_1 = matrix[y1][n - 1 - x1]
					matrix[y1][n - 1 - x1] = temp_num
					x1, y1 = y1,n - 1 - x1
					temp_num = temp_num_1
		return matrix

if __name__ == '__main__':
	sol = Solution()
	test_set = [
		[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
		[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
	]
	for test_data in test_set:
		print(sol.rotate(test_data))
