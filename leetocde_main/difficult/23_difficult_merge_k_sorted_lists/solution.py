# https://leetcode-cn.com/problems/merge-k-sorted-lists/
# 总的来说这题在python下要利用heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 速度实在太慢，写个直接把val值存在temp_node里的试试
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        temp_node = []  # 存储正在比较的各个节点指针
        new_head = ListNode()
        add_pointer = new_head  # 用于链接的指针
        for i in range(len(lists)):
            if lists[i] is not None:
                temp_node.append(lists[i])
        while True:
            n = len(temp_node)
            if n == 0:
                return new_head.next
            temp_min_index = 0  # 节点指针列表中最小的数对应的那个下标
            for i in range(1, n):
                if temp_node[i].val < temp_node[temp_min_index].val:
                    temp_min_index = i
            add_pointer.next = temp_node[temp_min_index]
            add_pointer = add_pointer.next
            # 判断取出指针的下一步是否有节点，有的话加入列表，没有的话删除
            if temp_node[temp_min_index].next:
                temp_node[temp_min_index] = temp_node[temp_min_index].next
            else:
                temp_node.pop(temp_min_index)
            add_pointer.next = None  # 其实不断开也可，写一下保险

    # 改进下temp_node尝试提速，还是慢的伤心 14%
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        temp_node = []  # 存储正在比较的各个节点指针
        temp_node_val = []
        new_head = ListNode()
        add_pointer = new_head  # 用于链接的指针
        for i in range(len(lists)):
            if lists[i] is not None:
                temp_node.append(lists[i])
                temp_node_val.append(lists[i].val)
        while True:
            n = len(temp_node)
            if n == 0:
                return new_head.next
            temp_min_index = 0  # 节点指针列表中最小的数对应的那个下标
            for i in range(1, n):
                if temp_node_val[i] < temp_node_val[temp_min_index]:
                    temp_min_index = i
            add_pointer.next = temp_node[temp_min_index]
            add_pointer = add_pointer.next
            # 判断取出指针的下一步是否有节点，有的话加入列表，没有的话删除
            if temp_node[temp_min_index].next:
                temp_node[temp_min_index] = temp_node[temp_min_index].next
                temp_node_val[temp_min_index] = temp_node[temp_min_index].val
            else:
                temp_node.pop(temp_min_index)
                temp_node_val.pop(temp_min_index)
            add_pointer.next = None  # 其实不断开也可，写一下保险


if __name__ == '__main__':
    for i in range(1, 1):
        print('hhh')
