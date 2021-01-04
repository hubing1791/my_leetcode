# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #这是递归法，迭代法先不管了
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build_helper(inorde: List[int]):
            # 先构造根节点
            x = preorder.pop(0)
            root = TreeNode(x)
            # 在中序遍历中取出左右子树
            index = inorde.index(x)
            left_inorder = inorde[:index]
            right_inorder = inorde[index + 1:]
            # 递归左右子树
            root.left = build_helper(left_inorder) if left_inorder else None
            root.right = build_helper(right_inorder) if right_inorder else None
            return root
        if not preorder:
            return None
        else:
            return build_helper(inorder)
