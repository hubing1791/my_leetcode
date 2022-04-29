# https://leetcode-cn.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    # 思路见官方解答
    # https://leetcode-cn.com/problems/maximum-product-subarray/solution/cheng-ji-zui-da-zi-shu-zu-by-leetcode-solution/
    def maxProduct(self, nums: List[int]) -> int:
        ans = min_temp = max_temp = nums[0]
        for i in nums[1:]:
            # 先得再次赋值
            min_temp_t,max_temp_t =min_temp,max_temp
            min_temp = min(i * min_temp_t, i, i * max_temp_t)
            max_temp = max(i * min_temp_t, i, i * max_temp_t)
            ans = max(ans, max_temp)
        return ans
