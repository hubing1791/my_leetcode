# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# 自己写的，思路是寻找节点，找到返回1，某个节点左右都返回1则既可以返回
	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		def find_node(root_node: TreeNode, p_node: TreeNode, q_node: TreeNode, result):
			if root_node is None:
				return 0
			left_flag = find_node(root_node.left, p_node, q_node, result)
			right_flag = find_node(root_node.right, p_node, q_node, result)
			if left_flag and right_flag:
				result.append(root_node)
				return 0
			elif left_flag or right_flag:
				# 此处第二版修改，为了应对某个节点即为公共的情况
				if root_node == p_node or root_node == q_node:
					result.append(root_node)
					return 0
				else:
					return 1
			else:
				if root_node == p_node or root_node == q_node:
					return 1
				else:
					return 0

		result_ = []
		find_node(root, p, q, result_)
		return result_[0]
