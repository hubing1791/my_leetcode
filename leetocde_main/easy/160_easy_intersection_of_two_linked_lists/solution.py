# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointA, pointB = headA, headB
        flagA = flagB = 1
        if not headA or not headB:
            return None
        while 1:
            if pointA == pointB:
                return pointA
            if not pointA.next and flagA:
                pointA = headB
                flagA = 0
            elif not pointA.next and not flagA:
                return None
            else:
                pointA = pointA.next
            if not pointB.next and flagB:
                pointB = headA
                flagB = 0
            elif not pointB.next and not flagB:
                return None
            else:
                pointB = pointB.next
