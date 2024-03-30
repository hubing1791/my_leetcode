# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
# 官方解答很简洁，以某个点作为树得到的值判断下是否是最大值，继续向上传的时候只能加左右子树中的一个
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


# 自己写的垃圾代码，仍然需要改进
class Solution:
	def maxPathSum(self, root: TreeNode) -> int:
		def max_sum(node: TreeNode, list1):
			if node.left:
				left_max = max_sum(node.left, list1)
			else:
				left_max = 0
			if node.right:
				right_max = max_sum(node.right, list1)
			else:
				right_max = 0
			if node.val < 0:
				if node.left and node.right:
					list1.append(max(left_max, right_max))
				elif node.left:
					list1.append(left_max)
				elif node.right:
					list1.append(right_max)
			if left_max < 0 and right_max < 0:
				node_num = node.val
			elif left_max < 0:
				node_num = node.val + right_max
			elif right_max < 0:
				node_num = node.val + left_max
			else:
				node_num = node.val + left_max + right_max
			return node_num

		max_list = []
		max_root = max_sum(root, max_list)
		if not max_list:
			return max_root
		else:
			return max(max(max_list), max_root)


class Solution:
	def __init__(self):
		self.maxSum = float("-inf")

	def maxPathSum(self, root: TreeNode) -> int:
		def maxGain(node):
			if not node:
				return 0

			# 递归计算左右子节点的最大贡献值
			# 只有在最大贡献值大于 0 时，才会选取对应子节点
			leftGain = max(maxGain(node.left), 0)
			rightGain = max(maxGain(node.right), 0)

			# 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
			priceNewpath = node.val + leftGain + rightGain

			# 更新答案
			self.maxSum = max(self.maxSum, priceNewpath)

			# 返回节点的最大贡献值
			return node.val + max(leftGain, rightGain)

		maxGain(root)
		return self.maxSum


if __name__ == '__main__':
	root_try = TreeNode(-3)
	sol = Solution()
	print(sol.maxPathSum(root_try))
