# https://leetcode-cn.com/problems/word-search/

from typing import List


class Solution:

	def exist(self, board: List[List[str]], word: str) -> bool:
		# m,n是位置，word_left是剩下未匹配的字符串
		def helper(m: int, n: int, word_left: str):
			if word_left == '':
				return True
			else:
				if board[m][n] != word_left[0]:
					return False
				else:
					flag = False
					temp = board[m][n]
					board[m][n] = '#'
					for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
						m1, n1 = m + x, n + y
						if m1 < 0 or n1 < 0 or m1 > len(board) - 1 or n1 > len(board[0]) - 1:
							if len(word_left) == 1:
								flag |= True
						else:
							flag |= helper(m1, n1, word_left[1:])
							if flag:
								break
					board[m][n] = temp
					return flag

		if not board and not board[0]:
			return False
		result_flag = False
		for i in range(len(board)):
			for j in range(len(board[0])):
				result_flag |= helper(i, j, word)
				if result_flag:
					return result_flag
		return result_flag


if __name__ == "__main__":
	test_set = [
		[[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"]
	]
	sol = Solution()
	for x, y in test_set:
		print(sol.exist(x, y))
