# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        # 从第二个数开始数，这样prev就不会重复比较
        index = 1
        prev = nums[0]
        count_num = 1
        while index < len(nums):
            if nums[index] == prev:
                count_num += 1
                index += 1
            else:
                prev = nums[index]
                index += 1
                count_num = 1
            if count_num == 3:
                nums.pop(index - 1)
                index -= 1
                count_num -= 1
        return len(nums)


if __name__ == "__main__":
    test_set = [
        [0, 0, 1, 1, 1, 1, 2, 3, 3]
    ]
    sol = Solution()
    for i in test_set:
        sol.removeDuplicates(i)
