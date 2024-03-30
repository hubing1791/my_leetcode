# https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
# 2022-05-05
from custom_moudle.initialize_data_struct.InitializeListNode import ListNode



class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		if not headA or not headB:
			return None
		flag_a, flag_b = 0, 0
		poiA, poiB = headA, headB
		while flag_a<2 or flag_b<2:
			if poiA == poiB:
				return poiA
			if poiA.next:
				poiA = poiA.next
			else:
				poiA = headB
				flag_a += 1
			if poiB.next:
				poiB = poiB.next
			else:
				poiB = headA
				flag_b += 1
		return None
