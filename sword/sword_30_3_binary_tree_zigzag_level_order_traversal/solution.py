# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
# 2022-04-27
from collections import deque
from typing import List

from custom_moudle.initialize_data_struct.InitializeTree import TreeNode

class Solution:
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		res = []
		if not root:
			return res
		node_list = deque([root])
		while node_list:
			tmp_result = deque()
			for _ in range(len(node_list)):
				tmp_node = node_list.popleft()
				if len(res) % 2 == 0:
					tmp_result.appendleft(tmp_node.val)
				else:
					tmp_result.append(tmp_node.val)
				if tmp_node.right:
					node_list.append(tmp_node.right)
				if tmp_node.left:
					node_list.append(tmp_node.left)
			res.append(list(tmp_result))
		return res