# https://leetcode.cn/problems/max-consecutive-ones-iii/
# 2022-11-20
from typing import List


class Solution:
    # 贪心加回溯 最初版写法有两个问题，无法处理k给的过高从而使得k+1的个数比长度大的情况，无法处理k=0的
    def longestOnes_1(self, nums: List[int], k: int) -> int:
        length = len(nums)
        one_left = k
        result, tmp_cum_value = 0, 0
        pointer, back_loc = 0, 0
        while pointer < length:
            if nums[pointer] == 0:
                one_left -= 1
            tmp_cum_value += 1
            pointer += 1
            if one_left == 0 and pointer < length and nums[pointer] == 0:
                result = max(result, tmp_cum_value)
                while nums[back_loc] == 1:
                    back_loc += 1
                while nums[back_loc] == 0:
                    back_loc += 1
                pointer = back_loc
                one_left = k
                tmp_cum_value = 0
        result = max(tmp_cum_value + one_left, result)
        return result

    # 官方解答第二个版本比较好，直接实现2了就
    def longestOnes_2(self, nums: List[int], k: int) -> int:
        left_sum, right_sum, ans, left_ptr = 0, 0, 0, 0
        for right in range(len(nums)):
            right_sum += 1 - nums[right]
            while right_sum - left_sum > k:
                left_sum += 1 - nums[left_ptr]
                left_ptr += 1
            ans = max(ans, right - left_ptr+1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    sol.longestOnes_2([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
