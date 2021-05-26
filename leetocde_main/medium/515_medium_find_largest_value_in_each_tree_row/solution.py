# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        level_order = deque([[root, 0]])
        result = []
        if not root:
            return result
        while level_order:
            node, level = level_order.popleft()
            if len(result) <= level:
                result.append(node.val)
            else:
                result[level] = max(result[level], node.val)
            if node.left:
                level_order.append([node.left, level + 1])
            if node.right:
                level_order.append([node.right, level + 1])
        return result
