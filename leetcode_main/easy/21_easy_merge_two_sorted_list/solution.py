# 2020-04-27
# https://leetcode-cn.com/problems/merge-two-sorted-lists/
from typing import Optional

from custom_moudle.initialize_data_struct.InitializeListNode import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head=cur = ListNode(0,None)
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        if not list1:
            cur.next = list2
        else:
            cur.next = list1
        return new_head.next