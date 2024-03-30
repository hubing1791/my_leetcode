# https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/




from collections import deque

from custom_moudle.initialize_data_struct.InitializeTree import TreeNode


class Solution:
	def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
		# 判断树是否相等,同时层序遍历,以node2为标准层序遍历
		def equal_tree(node1: TreeNode, node2: TreeNode):
			level_order1 = deque([node1])
			level_order2 = deque([node2])
			while level_order1 and level_order2:
				temp_node1 = level_order1.popleft()
				temp_node2 = level_order2.popleft()
				# 值不相等返回
				if temp_node1.val != temp_node2.val:
					return False
				# node2有的节点node1必须有，但是若node2没后文了
				# node1还是可以有的，所以要以node2为标准递归
				if temp_node2.left:
					if not temp_node1.left:
						return False
					else:
						level_order1.append(temp_node1.left)
						level_order2.append(temp_node2.left)
				if temp_node2.right:
					if not temp_node1.right:
						return False
					else:
						level_order1.append(temp_node1.right)
						level_order2.append(temp_node2.right)
			return True

		level_order = deque([A])
		b_root_val = B.val
		result = False
		while level_order:
			temp_node = level_order.popleft()
			if temp_node.val == b_root_val:
				result |= equal_tree(temp_node, B)
			if temp_node.left:
				level_order.append(temp_node.left)
			if temp_node.right:
				level_order.append(temp_node.right)
		return result
