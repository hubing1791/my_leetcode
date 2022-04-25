from typing import List

from custom_moudle.initialize_data_struct.InitializeListNode import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        result = []

        def helper(root: ListNode):
            if root.next:
                helper(root.next)
            result.append(root.val)

        if head:
            helper(head)
        return result
