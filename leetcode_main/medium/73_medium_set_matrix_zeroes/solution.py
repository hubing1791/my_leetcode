# https://leetcode-cn.com/problems/set-matrix-zeroes/
# 2021-09-17
from typing import List


class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		# 记录某个位置是否需要置为零的数组
		length, width = len(matrix), len(matrix[0])
		need_zero = [False] * (length + width)
		for i in range(length):
			for j in range(width):
				if matrix[i][j] == 0:
					need_zero[i], need_zero[length + j] = True, True
		for i in range(length):
			for j in range(width):
				if need_zero[i] or need_zero[length + j]:
					matrix[i][j] = 0

	# 实现一个空间消耗o(1)次的,思路是先改成-1，再改成0.
	# 此方法不可行，因为-1也会出现。python可以投机取巧取一个不存在的数，但是应该不是这题的考察点
	def setZeroes1(self, matrix: List[List[int]]) -> None:
		length, width = len(matrix), len(matrix[0])
		for i in range(length):
			for j in range(width):
				if matrix[i][j] == 0:
					for k in range(length):
						if matrix[k][j] != 0:
							matrix[k][j] = -1
					for k in range(width):
						if matrix[i][k] != 0:
							matrix[i][k] = -1
		for i in range(length):
			for j in range(width):
				if matrix[i][j] == -1:
					matrix[i][j] = 0

	# 看了题解的o(1)方法，有双标记和单标记法，双标记法就是直接把第一行第一列标0，来确定之后该行（列）是否需要置0，
	# 之所以需要额外的两个，是因为要考虑第一行第一列原本是否有0，双标记法就不用再遍历第一行和第一列了
	# 这儿实现单标记法。
	def setZeroes2(self, matrix: List[List[int]]) -> None:
		length, width = len(matrix), len(matrix[0])
		flag_cls = False
		for i in range(length):
			# 一开始这儿没有==0，写错了
			if matrix[i][0] == 0:
				flag_cls = True
			for j in range(1, width):
				if matrix[i][j] == 0:
					matrix[i][0], matrix[0][j] = 0, 0
		# range()里的第二个数一开始写成了0，少处理了第一行
		for i in range(length - 1, -1, -1):
			for j in range(1, width):
				if matrix[i][0] == 0 or matrix[0][j] == 0:
					matrix[i][j] = 0
		if flag_cls:
			for i in range(length):
				matrix[i][0] = 0


if __name__ == "__main__":
	test_set = [
		[[1, 1, 1], [1, 0, 1], [1, 1, 1]],
		[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
	]
	sol = Solution()
	for i in test_set:
		sol.setZeroes2(i)
		print(i)
