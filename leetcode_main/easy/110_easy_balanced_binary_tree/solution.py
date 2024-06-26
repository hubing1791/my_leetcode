# https://leetcode-cn.com/problems/balanced-binary-tree/
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isBalanced(self, root: TreeNode) -> bool:
		def tree_height(node: TreeNode):
			if not node:
				return 0
			left_height = tree_height(node.left)
			right_height = tree_height(node.right)
			if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
				return -1
			return max(left_height, right_height) + 1

		return tree_height(root) >= 0
