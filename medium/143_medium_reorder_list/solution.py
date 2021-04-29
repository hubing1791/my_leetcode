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
        pre, cur = fast.next, slow
        while cur:
            if not cur.next:
                rev_half = cur
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        cur_pre, cur_back = head, rev_half
        while cur_back:
            cur_pre_temp = cur_pre.next
            cur_back_temp = cur_back.next
            cur_pre.next = cur_back
            cur_back.next = cur_pre_temp
            cur_pre, cur_back = cur_pre_temp, cur_back_temp

    # 参考答案的第一版本
    def reorderList_1(self, head: ListNode) -> None:
        new_nodehead = head
        node_list = []
        while new_nodehead:
            node_list.append(new_nodehead)
            new_nodehead = new_nodehead.next
        leng_list = len(node_list)
        for i in range(leng_list // 2 - 1):
            node_list[i].next = node_list[-i - 1]
            node_list[-i - 1].next = node_list[i + 1]
        midd = leng_list // 2
        # 把最后几个
        if leng_list % 2 == 0:
            node_list[midd - 1].next = node_list[-midd]
            node_list[-midd].next = None
        else:
            node_list[midd - 1].next = node_list[-midd]
            node_list[-midd].next = node_list[midd]
            node_list[midd].next = None

    # 参考答案的第二版本
    def reorderList_2(self, head: ListNode) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        cur, pre = slow.next, None
        # 把前后链断开
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        # 这样结束后后半段的头就是此时的pre
        cur_left, cur_right = head, pre
        while cur_right:
            temp_left, temp_right = cur_left.next, cur_right.next
            cur_left.next, cur_right.next = cur_right, temp_left
            cur_left, cur_right = temp_left, temp_right
