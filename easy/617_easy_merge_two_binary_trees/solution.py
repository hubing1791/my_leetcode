# https://leetcode-cn.com/problems/merge-two-binary-trees/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 深度优先搜索
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            merge_node = TreeNode(t1.val + t2.val)
            merge_node.left = self.mergeTrees(t1.left, t2.left)
            merge_node.right = self.mergeTrees(t1.right, t2.right)
            return merge_node

    # 广度优先搜索，通过队列实现
    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            queue = [[t1, t2]]
            while queue:
                tree1, tree2 = queue.pop(0)
                tree1.val +=tree2.val
                if tree1.left and tree2.left:
                    queue.append([tree1.left,tree2.left])
                # 只要右树的子树不为空左子树为空需要接一下，另一种情况不管就行了
                elif tree2.left:
                    tree1.left = tree2.left
                if tree1.right and tree2.right:
                    queue.append([tree1.right,tree2.right])
                elif tree2.right:
                    tree1.right = tree2.right
        return t1
