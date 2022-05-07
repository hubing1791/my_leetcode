# https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/
# 2022-05-05
from custom_moudle.initialize_data_struct.InitializeTree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        result = True

        def DFS(node: TreeNode):
            nonlocal result
            if not node:
                return 0
            else:
                length_left = DFS(node.left)
                length_right = DFS(node.right)
                if abs(length_left - length_right) >= 2:
                    result = False
                    # 这时候返回啥都无所谓了，直接返回更快
                    return 0
                return max(length_right, length_left) +1

        DFS(root)
        return result
