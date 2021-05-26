# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        result = []
        while left <= right:
            med = (left + right) // 2
            # 找到相等的就在前后搜索找位置
            if nums[med] == target:
                while med >= 0:
                    if nums[med] == target:
                        med -= 1
                    else:
                        break
                med += 1
                result.append(med)
                while med <= len(nums) - 1:
                    if nums[med] == target:
                        med += 1
                    else:
                        break
                med -= 1
                result.append(med)
                return result
            elif target < nums[med]:
                right = med - 1
            else:
                left = med + 1
        return [-1, -1]
