# https://leetcode-cn.com/problems/next-greater-element-ii/
from typing import List


class Solution:
    # 利用单调栈
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        length = len(nums)
        result = [-1] * length
        for i in range(length*2-1,-1,-1):
            while stack and nums[i%length]>=nums[stack[-1]]:
                stack.pop()
            result[i%length] = -1 if not stack else nums[stack[-1]]
            stack.append(i%length)
        return result
