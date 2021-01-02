# https://leetcode-cn.com/problems/reverse-nodes-in-k-group

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 参考了答案，一开始写的逻辑混乱
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 传入头尾节点进行置换的函数
        def reverse_linklist(head_node: ListNode, tail_node: ListNode, m: int):
            pre, cur = tail_node.next, head_node  # 前面的那个节点和正在用于交换的节点
            for i in range(m):
                pre, cur.next, cur = cur, pre, cur.next
            return tail_node, head_node

        temp = new_head = ListNode(0, head)
        while temp.next:
            cur_node = temp.next
            for i in range(k - 1):
                cur_node = cur_node.next
                if not cur_node:
                    return new_head.next
            reverse_head, reverse_tail = reverse_linklist(temp.next, cur_node, k)
            temp.next = reverse_head
            temp = reverse_tail
        return new_head.next


if __name__ == "__main__":
    curr = head = ListNode(1)
    for i in range(2, 6):
        node = ListNode(i)
        curr.next = node
        curr = curr.next
    sol = Solution()
    curr = sol.reverseKGroup(head, 2)
    while curr:
        print(curr.val)
        curr = curr.next
