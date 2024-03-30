# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
from custom_moudle.initialize_data_struct.InitializeTree import TreeNode


class Solution:
	# 迭代加保存之前访问的节点，从而在一次遍历中完成
	def flatten(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		if not root:
			return None
		stack = [root]
		prev = None
		while stack:
			cur = stack.pop()
			if prev:
				prev.left = None
				prev.right = cur
			if cur.right:
				stack.append(cur.right)
			if cur.left:
				stack.append(cur.left)
			prev = cur

	# o(1)复杂度,
	def flatten(self, root: TreeNode) -> None:
		cur = root
		while cur:
			# 重连之后，也会再次因为一直right，从而开始遍历右子树
			if cur.left:
				prev = nxt = cur.left
				while prev.right:
					prev = prev.right
				prev.right = cur.right
				cur.left = None
				cur.right = nxt
			cur = cur.right
