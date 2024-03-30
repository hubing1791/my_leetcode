class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	# 这一版遇到[1],1会出问题
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		cycle_index = 0
		del_node, cycle_node = head, head

		while True:
			if cycle_node.next is None:  # 在这个位置，会出问题
				del_node.next = del_node.next.next
				break
			cycle_index += 1
			cycle_node = cycle_node.next
			if cycle_index >= n + 1:
				del_node = del_node.next
		return head

	# 通过添加一个头指针可以解决
	def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
		cycle_index = 0
		new_head = ListNode(0)
		new_head.next = head
		slow, fast = new_head, new_head

		while True:
			fast = fast.next
			cycle_index += 1
			if cycle_index > n + 1:
				slow = slow.next
			if not fast:
				slow.next = slow.next.next
				break
		return new_head.next
