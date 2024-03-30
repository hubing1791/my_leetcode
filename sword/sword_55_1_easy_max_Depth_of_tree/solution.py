# https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
# 2022-05-05
from custom_moudle.initialize_data_struct.InitializeTree import TreeNode


class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		result = 0

		def DFS(node: TreeNode, depth: int):
			nonlocal result
			if not node:
				result = max(depth, result)
			else:
				DFS(node.left, depth + 1)
				DFS(node.right, depth + 1)

		DFS(root,0)
		return result
