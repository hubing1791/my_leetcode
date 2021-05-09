# https://leetcode-cn.com/problems/validate-binary-search-tree/
import sys

sys.path.append("..")
from some_practice.initialize_data_struct.InitializeTree import TreeNode
from some_practice.initialize_data_struct.InitializeTree import InitializeTree


class Solution:
    # 中序遍历的迭代版
    def isValidBST(self, root: TreeNode) -> bool:
        stack, result_list, temp_node = [], [], root
        while stack or temp_node:
            if temp_node:
                stack.append(temp_node)
                temp_node = temp_node.left
            else:
                temp_node = stack.pop()
                if result_list:
                    if temp_node.val < result_list[-1]:
                        return False
                result_list.append(temp_node.val)
                temp_node = temp_node.right
        return True

    # 递归实现
    def isValidBST_1(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode, lower=float('-inf'), higher=float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= higher:
                return False
            else:
                return dfs(node.left, lower, node.val) and dfs(node.right, node.val, higher)

        return dfs(root)


if __name__ == "__main__":
    sol = Solution()
    test_set = [5, 1, 4, None, None, 3, 6]
    root = InitializeTree(test_set)
    sol.isValidBST(root)
