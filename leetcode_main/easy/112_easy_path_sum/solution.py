# https://leetcode-cn.com/problems/path-sum/

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# 这版错在了，判断是否对在下一步节点了，对[1,2]这样的，只有一个叶子节点，这个算法会把根节点既当作根又当作叶子
	def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		def helper(node: TreeNode, sums: int):
			if not node and sums == 0:
				return True
			elif not node and sums != 0:
				return False
			flag_left = helper(node.left, sums - node.val)
			flag_right = helper(node.right, sums - node.val)
			return flag_left | flag_right

		if not root:
			return False
		else:
			return helper(root, sum)

	def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
		def helper(node: TreeNode, sums: int):
			if not node.left and not node.right:
				return (sums - node.val) == 0
			elif node.right and node.left:
				return helper(node.right, sums - node.val) | helper(node.left, sums - node.val)
			elif not node.left:
				return helper(node.right, sums - node.val)
			else:
				return helper(node.left, sums - node.val)

		if not root:
			return False
		else:
			return helper(root, sum)
