# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 一开始想用两个遍历对比，但是实际上行不通
# 参考了官方的解法，在左右子树对称的扫描
class Solution:
    def ComparelandR(self, left_tree: TreeNode, right_tree: TreeNode):
        if left_tree is None and right_tree is None:
            return True
        elif left_tree is None or right_tree is None:
            return False
        elif left_tree.val != right_tree.val:
            return False
        return self.ComparelandR(left_tree.left, right_tree.right) and self.ComparelandR(left_tree.right, right_tree.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.ComparelandR(root.left, root.right)
