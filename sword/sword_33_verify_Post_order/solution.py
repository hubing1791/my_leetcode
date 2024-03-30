# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
# 2022-04-27
from typing import List


class Solution:
	def verifyPostorder(self, postorder: List[int]) -> bool:
		def check(i: int, j: int):
			if j - i <= 1:
				return True
			root = postorder[j]
			index = i
			# 找到左右子树的分界点
			while postorder[index] < root:
				index += 1
			for ind in range(index, j):
				if postorder[ind] < root:
					return False
			return check(i, index - 1) and check(index, j - 1)

		return check(0, len(postorder) - 1)
