# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
# 2021-10-01

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque


class Solution:
    # 先实现一个二叉树层序遍历改，这个方法使用o(n)的额外空间
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        # 遍历过程中保存之前的节点，用户连接，层数相同就连，不同就null
        fore_node = [root, 0]
        node_list = deque([[root, 0]])
        while node_list:
            temp_node = node_list.popleft()
            if temp_node[0].left:
                node_list.append([temp_node[0].left, temp_node[1] + 1])
            if temp_node[0].right:
                node_list.append([temp_node[0].right, temp_node[1] + 1])
            if fore_node[1]:
                if fore_node[1] == temp_node[1]:
                    fore_node[0].next = temp_node[0]
            # 一开始将接下来的这行写进了if，而初始的fore_node[1]为0,永远不执行也不更新
            fore_node = temp_node
        return root

    # 这题参考了题解，可以利用已经建立好的next，从而实现o(1)的空间复杂度
    def connect1(self, root: Node) -> Node:
        if not root:
            return root
        # left_most 表示每一层循环中的最左节点
        left_most = root
        while left_most:
            temp_node = left_most
            # 左右节点都存在直接连上
            while temp_node:
                if temp_node.left and temp_node.right:
                    temp_node.left.next = temp_node.right
                if temp_node.right and temp_node.next and temp_node.next.left:
                    temp_node.right.next = temp_node.next.left
                temp_node = temp_node.next
            left_most = left_most.left
        return root
