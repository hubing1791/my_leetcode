# https://leetcode-cn.com/problems/spiral-matrix/
from typing import List


class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		result = []
		if not matrix:
			return result
		length_cycle, width_cycle = length, width = len(matrix[0]), len(matrix)
		while length_cycle and width_cycle:
			if length_cycle > 1 and width_cycle > 1:
				a = (width - width_cycle) // 2  # 竖方向的起始位置
				b = (length - length_cycle) // 2  # 横方向起始位置
				for i in range(length_cycle):
					result.append(matrix[a][b + i])
				for i in range(1, width_cycle - 1):  # 因为竖方向已经有一个位置被上个循环取过了，要排除
					result.append(matrix[a + i][b + length_cycle - 1])
				for i in range(length_cycle):
					result.append(matrix[width - a - 1][-b - i - 1])
				for i in range(1, width_cycle - 1):
					result.append(matrix[-a - i - 1][b])
				length_cycle -= 2
				width_cycle -= 2
			else:
				b = (length - length_cycle) // 2
				a = (width - width_cycle) // 2
				if width_cycle == 1:
					for i in range(length_cycle):
						result.append(matrix[a][b + i])
					width_cycle -= 1
				else:
					for i in range(width_cycle):
						result.append(matrix[a + i][b])
					length_cycle -= 1
		return result


if __name__ == '__main__':
	# test_set = [[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]]
	#			 ]
	# sol = Solution()
	# for x, y in test_set:
	#	 print(str(sol.spiralOrder(x)) + '\t' + str(y))
	for i in range(0,-10,-1):
		print(i)
		if i :
			print('hhhhhh')
