# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

from typing import List


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		stack, result = [], []
		while stack or root:
			if root:
				stack.append(root)
				root = root.left
			else:
				root = stack.pop()
				result.append(root.val)
				root = root.right
		return result
