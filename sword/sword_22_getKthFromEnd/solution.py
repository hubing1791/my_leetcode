# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
# 2022-04-27
from custom_moudle.initialize_data_struct.InitializeListNode import ListNode


class Solution:
	def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
		start, end = head, head
		for i in range(k):
			end = end.next
		while end:
			start = start.next
			end = end.next

		return start
