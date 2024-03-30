# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
# 2022-05-05
from custom_moudle.initialize_data_struct.InitializeTree import TreeNode
from collections import deque

class Solution:
	def kthLargest(self, root: TreeNode, k: int) -> int:
		stack = []
		queue = deque([0]*k)
		node = root
		while stack or node:
			while node:
				stack.append(node)
				node = node.left
			node = stack.pop()
			queue.popleft()
			queue.append(node.val)
			node = node.right
		return queue[0]
