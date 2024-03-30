# https://leetcode-cn.com/problems/reverse-linked-list-ii/

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
		# 添加头节点使得left无左节点也可以同样处理
		left_pre = new_head = ListNode(val=-1, next=head)
		left_node = head
		# 寻找left前节点和left
		count = 1
		while count < left:
			left_pre = left_pre.next
			left_node = left_node.next
			count += 1
		# 寻找right和right的后向节点
		count = 0
		right_node, right_next = new_head, head
		while count < right:
			right_node = right_node.next
			right_next = right_next.next
			count += 1
		# 把链表断出来
		right_node.next = None
		pre, cur = right_next, left_node
		while cur:
			temp = cur.next
			cur.next = pre
			pre = cur
			cur = temp
		left_pre.next = right_node
		return new_head.next

	def reverseBetween_1(self, head: ListNode, left: int, right: int) -> ListNode:
		right_node = left_pre = new_head = ListNode(val=-1, next=head)
		right_next = left_node = head
		count = 0
		while count < right:
			if count < left - 1:
				left_pre = left_pre.next
				left_node = left_node.next
			right_node = right_node.next
			right_next = right_next.next
			count += 1
		right_node.next = None
		pre, cur = right_next, left_node
		while cur:
			temp = cur.next
			cur.next = pre
			pre = cur
			cur = temp
		left_pre.next = right_node
		return new_head.next
