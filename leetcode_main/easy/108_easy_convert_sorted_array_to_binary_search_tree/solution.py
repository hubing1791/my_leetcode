# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.

from typing import List


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# 参考了答案思路
	def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
		def build_node(left, right):
			if left > right:
				return None
			mid = (left + right) / 2
			node = TreeNode(nums[mid])
			node.left = build_node(left, mid - 1)
			node.right = build_node(mid + 1, right)
			return node

		build_node(0, len(nums))
