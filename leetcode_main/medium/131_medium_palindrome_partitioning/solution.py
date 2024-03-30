# https://leetcode-cn.com/problems/palindrome-partitioning/
# 2021-11-08

from typing import List


# 看题解写的
class Solution:
	def partition(self, s: str) -> List[List[str]]:
		n = len(s)
		judge_matrix = [[True] * n for _ in range(n)]
		# 第一个i表示的是长度，和自己本身比的已经相当于初始化过了，没必要
		for i in range(1, n):
			j = 1
			# 像下面这样写，只会生成奇数长度对应的结果
			# while i-j >=0 and i+j < n:
			#	 judge_matrix[i-j][i+j]=
			for j in range(n - i):
				judge_matrix[j][j + i] = (s[j] == s[j + i]) and judge_matrix[j + 1][j + i - 1]

		result = []
		temp_ans = []

		# 传入位置
		def dfs(index: int):
			if index == n:
				# 这种写法不对，会使得加入result的其实是两个指向temp_ans的对象，最后都会被清空
				# result.append(temp_ans)
				result.append(temp_ans[:])
				return
			for i in range(index, n):
				if judge_matrix[index][i]:
					temp_ans.append(s[index:i + 1])
					dfs(i+1)
					temp_ans.pop()

		dfs(0)
		return result
