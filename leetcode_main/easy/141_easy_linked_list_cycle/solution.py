# https://leetcode-cn.com/problems/linked-list-cycle/


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# 利用hash表的o(n),o(n)
	def hasCycle(self, head: ListNode) -> bool:
		node_hash = set()
		while head:
			if head in node_hash:
				return True
			else:
				node_hash.add(head)
				head = head.next
		return False

	# 利用快慢指针
	def hasCycle2(self, head: ListNode) -> bool:
		if not head or not head.next:
			return False
		slow, fast = head, head.next
		while slow != fast:
			# 防止访问越界
			if not fast or not fast.next:
				return False
			else:
				slow = slow.next
				fast = fast.next.next
		return True
