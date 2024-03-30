# https://leetcode-cn.com/problems/valid-sudoku/
# 2021-09-09

from typing import List


class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		sets = []
		for i in range(27):
			sets.append(set())
		for i in range(0, 9):
			for j in range(0, 9):
				if board[i][j] != ".":
					if board[i][j] in sets[i] or board[i][j] in sets[9 + j] or \
							board[i][j] in sets[18 + (i // 3) * 3 + j // 3]:
						return False
					else:
						sets[i].add(board[i][j])
						sets[9 + j].add(board[i][j])
						sets[18 + (i // 3) * 3 + j // 3].add(board[i][j])
		return True


if __name__ == "__main__":
	test_set = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
				[".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
				["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
				[".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
				[".", ".", ".", ".", "8", ".", ".", "7", "9"]]
	sol = Solution()
	sol.isValidSudoku(test_set)
