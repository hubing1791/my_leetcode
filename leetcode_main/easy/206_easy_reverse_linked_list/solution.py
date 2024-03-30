# https://leetcode-cn.com/problems/reverse-linked-list/
# Definition for singly-linked list.
from custom_moudle.initialize_data_struct.InitializeListNode import ListNode, InitLL


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


class Solution1:
	def reverseList_wrong(self, head: ListNode) -> ListNode:
		prev, cur = None, head
		while cur.next:
			# 平行赋值不对
			# 平行赋值的原理是先计算右边的值，在按顺序赋值给左边
			prev, cur, cur.next = cur, cur.next, prev
		cur.next = prev
		return cur


if __name__ == '__main__':
	head = InitLL([1, 2, 3, 4, 5])
	so=Solution1()
	so.reverseList_wrong(head)
