# https://leetcode-cn.com/problems/invert-binary-tree/
from custom_moudle.initialize_data_struct.InitializeTree import TreeNode


class Solution:
    # 用深度优先可以很轻松解决
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(tree_node: TreeNode):
            if tree_node.left and tree_node.right:
                templeft, tempright = tree_node.left, tree_node.right
                tree_node.left = dfs(tempright)
                tree_node.right = dfs(templeft)
                return tree_node
            elif tree_node.left and not tree_node.right:
                tree_node.right = dfs(tree_node.left)
                tree_node.left =None
                return tree_node
            elif not tree_node.left and tree_node.right:
                tree_node.left = dfs(tree_node.right)
                tree_node.right  = None
                return tree_node
            else:
                return tree_node
        return dfs(root) if root else root
