# https://leetcode-cn.com/problems/swap-nodes-in-pairs/
from custom_moudle.initialize_data_struct.InitializeListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = temp = ListNode(next=head)
        while temp and temp.next:
            if temp.next.next:
                # 重新赋值方便阅读
                node1 = temp.next
                node2 = temp.next.next
                tail = temp.next.next.next
                # 此时的temp就是上一轮的头
                temp.next = node2
                node2.next = node1
                node1.next = tail
                temp = node1
            else:
                break
        return new_head.next

