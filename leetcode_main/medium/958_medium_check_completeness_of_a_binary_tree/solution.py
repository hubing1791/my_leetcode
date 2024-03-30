# https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isCompleteTree(self, root: TreeNode) -> bool:
		node_list = [[root, 1]]
		# 层序遍历结果
		level_result = []
		while node_list:
			node_temp = node_list.pop(0)
			level_result.append(node_temp[1])
			if node_temp[0].left:
				node_list.append([node_temp[0].left,2*node_temp[1]])
			if node_temp[0].right:
				node_list.append([node_temp[0].right,2*node_temp[1]+1])
		length = len(level_result)
		return level_result[length - 1] == length
