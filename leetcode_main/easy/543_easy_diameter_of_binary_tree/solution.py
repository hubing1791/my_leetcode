# https://leetcode-cn.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# 直接递归完事
	def diameterOfBinaryTree(self, root: TreeNode) -> int:
		result = 0

		def helper(node: TreeNode):
			nonlocal result
			if node is None:
				return 0
			left_max = helper(node.left)
			right_max = helper(node.right)
			if (left_max + right_max) > result:
				result = left_max + right_max
			return max(left_max,right_max) + 1
		helper(root)
		return result
