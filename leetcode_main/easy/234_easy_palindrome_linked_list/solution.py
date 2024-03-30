# https://leetcode-cn.com/problems/palindrome-linked-list/
from custom_moudle.initialize_data_struct.InitializeListNode import ListNode


class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		slow = fast = head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
		# 取出右半段并断链
		pre, cur = None, slow.next
		slow.next = None
		right = None
		while cur:
			temp = cur.next
			if not temp:
				right = cur
			cur.next = pre
			pre = cur
			cur = temp
		left = head
		while left and right:
			if left.val != right.val:
				return False
			else:
				left = left.next
				right = right.next
		return True
