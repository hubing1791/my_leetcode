# https://leetcode-cn.com/problems/binary-tree-right-side-view/
from typing import List


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# 直接想到了利用特殊的层序遍历来实现
	# 改用deque比list快，因为deque实际上在移动指针
	def rightSideView(self, root: TreeNode) -> List[int]:
		level_order_list = [[root, 1]]  # 保存节点和对应的层
		result_list = []
		if not root:
			return result_list
		while level_order_list:
			temp_node, level = level_order_list[0]
			level_order_list.pop(0)
			if temp_node.left:
				level_order_list.append([temp_node.left, level + 1])
			if temp_node.right:
				level_order_list.append([temp_node.right, level + 1])
			if len(result_list) < level:
				result_list.append(temp_node.val)
			else:
				result_list[level - 1] = temp_node.val
			if not level_order_list:
				return result_list
