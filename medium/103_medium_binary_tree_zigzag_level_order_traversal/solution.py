# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversa
# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        cycle_list = deque([[root, 0]])  # 用于层序遍历的数组。数组的每一项是节点和层数
        result = []
        if not root:
            return result
        while cycle_list:
            x, y = cycle_list[0]  # 取出节点值和层数
            if len(result) <= y:
                result.append([x.val])
            else:
                result[y].append(x.val)
            cycle_list.popleft()
            if x.left:
                cycle_list.append([x.left, y + 1])
            if x.right:
                cycle_list.append([x.right, y + 1])
        for i in range(result):
            if i % 2 == 1:
                result[i] = list(reversed(result[i]))
        return result
