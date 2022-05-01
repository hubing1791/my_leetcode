# https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
# 2022-04-30

from collections import defaultdict


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_2_node = defaultdict(lambda: None)
        copy_new_head = Node(0)
        cur_origin, prev_copy, cur_copy = head, copy_new_head, None
        # 用原本的进行遍历，完成第一遍复制
        while cur_origin:
            cur_copy = Node(cur_origin.val)
            node_2_node[cur_origin] = cur_copy
            prev_copy.next = cur_copy
            prev_copy = cur_copy
            cur_origin = cur_origin.next
        # 第二遍补完random
        cur_copy = copy_new_head.next
        cur_origin = head
        while cur_origin:
            if cur_origin.random:
                cur_copy.random = node_2_node[cur_origin.random]
            else:
                cur_copy.random = None
            cur_copy, cur_origin = cur_copy.next, cur_origin.next
        return copy_new_head.next

    # 官方解答的第一种，和我的实际等价，回溯加hash
    def copyRandomList_off1(self, head: 'Node') -> 'Node':
        node_2_node = defaultdict(lambda: None)

        def helper(node: Node):
            if not node:
                return None
            if not node_2_node[node]:
                node_copy = Node(node.val)
                node_2_node[node] = node_copy
                node_copy.next = helper(node.next)
                node_copy.random = helper(node.random)
            return node_2_node[node]

        return helper(head)

    # 官方第二种方法
    def copyRandomList_off2(self, head: 'Node') -> 'Node':
        if not head:
            return head
        node_origin = head
        # 第一遍，复制并插入
        while node_origin:
            node_copy = Node(node_origin.val)
            node_copy.next = node_origin.next
            node_origin.next = node_copy
            node_origin = node_copy.next
        node_origin = head
        # 第二遍，填充复制好的节点的random
        while node_origin:
            if node_origin.random:
                node_origin.next.random = node_origin.random.next
            node_origin = node_origin.next.next
        # 第三遍,把结果断出来
        node_origin =head
        prev = node_origin
        cur = node_origin.next
        while cur:
            prev.next = cur
            if cur.next and cur.next.next:
                prev = cur
                cur = cur.next.next
            else:
                break
        return head.next
