# https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
# 2020-04-29
from collections import defaultdict, deque
from typing import List

from custom_moudle.initialize_data_struct.InitializeTree import TreeNode


class Solution:
	# 方法可以改进，通过入栈出栈避免使用完整副本。但是搞笑的是改完了平台上效果变差了
	def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
		result = []

		def helper(node: TreeNode, num_left: int, node_list: List[int]):
			node_list.append(node.val)
			# 要求是根节点到叶子节点，因此还要判断左右子节点是否为空
			if num_left == node.val and not node.left and not node.right:
				result.append(node_list[:])
				node_list.pop()
				return
			else:
				# 一开始想当然以为是正数了
				if node.left:
					helper(node.left, num_left - node.val, node_list[:])
				if node.right:
					helper(node.right, num_left - node.val, node_list[:])
				node_list.pop()
				return

		if root:
			helper(root, target, [])
		return result

	# 建好一个查父节点的表，然后实际上就是一个层序遍历+额外存储节点对应的当前结果值，每次出队列都进行比较
	def pathSum_bfs(self, root: TreeNode, target: int) -> List[List[int]]:
		result = []
		parent = defaultdict(lambda: None)

		def get_result(node: TreeNode):
			tmp_result = []
			while node:
				tmp_result.append(node.val)
				node = parent[node]
			result.append(tmp_result[::-1])
			return

		if not root:
			return result

		node_queue = deque([root])
		sum_queue = deque([0])

		while node_queue:
			tmp_node = node_queue.popleft()
			tmp_sum = sum_queue.popleft() + tmp_node.val
			if not tmp_node.left and not tmp_node.right and tmp_sum == target:
				get_result(tmp_node)
			if tmp_node.left:
				node_queue.append(tmp_node.left)
				parent[tmp_node.left] = tmp_node
				sum_queue.append(tmp_sum)
			if tmp_node.right:
				node_queue.append(tmp_node.right)
				parent[tmp_node.right] = tmp_node
				sum_queue.append(tmp_sum)
		return result

# 错误版本,因为python传入列表是引用
class SolutionWrong:
	def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
		def helper(node: TreeNode, num_left: int, node_list: List[int]):
			if num_left == node.val:
				node_list.append(node.val)
				return [[True, node_list]]
			elif num_left > node.val:
				tmp_result = []
				node_list.append(node.val)
				if node.left:
					for re_tmp in helper(node.left, num_left - node.val, node_list):
						if re_tmp[0]:
							tmp_result.append(re_tmp)
				if node.right:
					for re_tmp in helper(node.right, num_left - node.val, node_list):
						if re_tmp[0]:
							tmp_result.append(re_tmp)
				return tmp_result
			else:
				return [[False, []]]

		results = []
		if root:
			results = helper(root, target, [])
		true_results = []
		for result in results:
			if result[0]:
				true_results.append(result[1])
		return true_results


if __name__ == '__main__':
	def dd():
		return 5


	dic = defaultdict(lambda:5)
	dic['bbb'] = 3
	print(dic['bbb'])
