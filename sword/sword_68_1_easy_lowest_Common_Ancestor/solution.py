# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
# 2022-05-07
from custom_moudle.initialize_data_struct.InitializeTree import TreeNode


class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		result = root
		p_val, q_val = p.val, q.val
		while 1:
			if result.val < p_val and result.val < q_val:
				result = result.right
			elif result.val > p_val and result.val > q_val:
				result = result.left
			else:
				break
		return result
