# https://leetcode-cn.com/problems/linked-list-cycle-ii/
from custom_moudle.initialize_data_struct.InitializeListNode import ListNode


class Solution:
	# 节点入列表，重复就跳出返回，不然循环到结束返回
	# 一开始用list以为要返回位置，后来发现只需要节点，改list为set
	def detectCycle(self, head: ListNode) -> ListNode:
		node_list = set()
		node_pointer = head
		while node_pointer:
			if node_pointer in node_list:
				return node_pointer
			else:
				node_list.add(node_pointer)
				node_pointer = node_pointer.next
		return None

	# https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/
	# 快慢指针法更多是思路比较重要，写起来容易多了
	def detectCycleFastSlow(self, head: ListNode) -> ListNode:
		slow = fast = head
		while slow and fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				new_ptr = head
				while slow != new_ptr:
					slow = slow.next
					new_ptr = new_ptr.next
				return slow
		return None
