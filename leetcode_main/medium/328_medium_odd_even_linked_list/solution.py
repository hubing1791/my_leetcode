# https://leetcode-cn.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	# 我一开始想加一个标志位，完全没必要
	def oddEvenList(self, head: ListNode) -> ListNode:
		if not head:
			return head
		even_head = head.next
		odd,even = head,head.next
		while even and even.next:
			odd.next = even.next
			odd = odd.next
			even.next = odd.next
			even = even.next
		odd.next = even_head
		return head


