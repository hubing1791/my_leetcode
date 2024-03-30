# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 2022-05-07
from custom_moudle.initialize_data_struct.InitializeTree import TreeNode
from collections import defaultdict


class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		father_dict = defaultdict(lambda: None)

		def DFS_F(node: TreeNode):
			if node.left:
				father_dict[node.left] = node
				DFS_F(node.left)
			if node.right:
				father_dict[node.right] = node
				DFS_F(node.right)

		DFS_F(root)

		def F_L(node: TreeNode):
			result = [node]
			tmp_father = father_dict[node]
			while tmp_father:
				result.append(tmp_father)
				tmp_father = father_dict[tmp_father]
			return result

		father_p = F_L(p)
		father_q = F_L(q)
		length = min(len(father_p), len(father_q))
		result = None
		for i in range(-1, -length - 1, -1):
			if father_q[i] == father_p[i]:
				result = father_q[i]
			else:
				break
		return result
