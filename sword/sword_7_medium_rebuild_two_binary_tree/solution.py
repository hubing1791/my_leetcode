# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/

from typing import List

from custom_moudle.initialize_data_struct.InitializeTree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            # 终止循环的条件
            if preorder_left > preorder_right:
                return None
            # 建立节点
            num_root = preorder[preorder_left]
            root = TreeNode(num_root)
            # 定位中序序列中根节点位置
            inorder_index = inorder_indexs[num_root]
            # 计算左子树节点数
            num_left = inorder_index - inorder_left
            root.left = helper(preorder_left + 1, preorder_left + num_left, inorder_left, inorder_index - 1)
            root.right = helper(preorder_left + num_left + 1, preorder_right, inorder_index + 1, inorder_right)
            return root

        inorder_indexs = {numbers: i for i, numbers in enumerate(inorder)}
        n = len(preorder)
        return helper(0, n - 1, 0, n - 1)
