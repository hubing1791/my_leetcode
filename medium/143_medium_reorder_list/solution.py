# https://leetcode-cn.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 整体思路没问题，但是这样写找出的后半段可能反转后会出现公共节点，就会出问题。
    def reorderList(self, head: ListNode) -> None:
        slow = fast = head
        while 1:
            if fast.next:
                fast = fast.next
                slow = slow.next
                if fast.next:
                    fast = fast.next
            else:
                break
        pre,cur = fast.next,slow
        while cur:
            if not cur.next:
                rev_half = cur
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        cur_pre,cur_back = head,rev_half
        while cur_back:
            cur_pre_temp = cur_pre.next
            cur_back_temp = cur_back.next
            cur_pre.next = cur_back
            cur_back.next = cur_pre_temp
            cur_pre, cur_back = cur_pre_temp,cur_back_temp

    # 参考答案的第一班
    def reorderList_1(self, head: ListNode) -> None:
        new_nodehead = head
        node_list = []
        while new_nodehead:
             
