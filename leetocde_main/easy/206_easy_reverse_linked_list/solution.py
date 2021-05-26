# https://leetcode-cn.com/problems/reverse-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre, cur = None, head
        while cur:
            if not cur.next:
                result = cur
                # 这一步要注意，巧妙返回新的头
            pre, cur.next, cur = cur, pre, cur.next
        return result
