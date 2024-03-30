# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	# 迭代版本
	def treeToDoublyList(self, root: Node) -> Node:
		if not root:
			return root
		stack, result_list, cur_node = [], [], root
		while stack or cur_node:
			if cur_node:
				stack.append(cur_node)
				cur_node = cur_node.left
			else:
				cur_node = stack.pop()
				result_list.append(cur_node)
				cur_node = cur_node.right
		length = len(result_list)
		# 把中间节点连接好
		for i in range(1, length - 1):
			result_list[i].left = result_list[i - 1]
			result_list[i].right = result_list[i + 1]
		# 首尾相连
		if length > 1:
			result_list[0].right = result_list[1]
			result_list[0].left = result_list[-1]
			result_list[-1].left = result_list[-2]
			result_list[-1].right = result_list[0]
		# 长度只有1的话自己连自己
		if length == 1:
			result_list[0].left = result_list[0]
			result_list[0].right = result_list[0]
		head = result_list[0]
		return head


	# 递归版本
	def treeToDoublyList_1(self, root):

		def dfs(cur):
			nonlocal head, pre
			if not cur:
				return
			dfs(cur.left)
			if pre:
				pre.right, cur.left = cur, pre
			else:
				head = cur
			pre = cur
			dfs(cur.right)

		if not root:
			return
		pre, head = None, None
		dfs(root)
		pre.right, head.left = head, pre
		return head
