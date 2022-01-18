# https://leetcode-cn.com/problems/3sum-closest/
# 2021-12-17
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        # 根据target的取值范围来看，差值不可能比20000还大
        difference = 20000
        result = []
        for i in range(len(nums) - 2):
            # 这段没有必要，会对下面所用的测例产生影响，结果不对
            # if nums[i] > target // 3:
            #     break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, length - 1
            while left < right:
                difference_temp = abs(target - nums[i] - nums[left] - nums[right])
                if difference_temp < difference:
                    difference = difference_temp
                    result = [nums[i], nums[left], nums[right]]
                if nums[i] + nums[left] + nums[right] <= target:
                    left += 1
                    # 之前没加下面这两行，又重复计算,and左边条件不屑会溢出，写道右边也会溢出
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    test_set = [
        [[1, 1, 1, 1], 0]
    ]
    for nums, target in test_set:
        sol.threeSumClosest(nums, target)
