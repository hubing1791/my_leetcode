# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 定义一个辅助的中序遍历
        number = 0
        result = 0

        def inroder_helper(node: TreeNode):
            nonlocal number
            nonlocal result
            if not node:
                return False

            flag = inroder_helper(node.left)
            # 剪枝
            if flag:
                return True

            number += 1
            if number == k:
                result = node.val
                return True

            flag = inroder_helper(node.right)
            return flag

        inroder_helper(root)
        return result
