# https://leetcode-cn.com/problems/trapping-rain-water/
from typing import List


class Solution:
    # 官方解法第二种
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        if n <= 2:
            return 0
        left_max, right_max = [0] * n, [0] * n
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])
        for i in range(-2, -n, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(1, n - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans

    # 官方第三种解法写一半不想写了先放弃
    def trap2(self, height: List[int]) -> int:
        stack = []
        n = len(height)
        ans = 0
        if n <= 2:
            return 0
        cycle_index = 0
        while cycle_index <= n - 1:
            pass


if __name__ == '__main__':
    sol = Solution()
    test_set = [
        [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
        [[4, 2, 0, 3, 2, 5], 9]
    ]
    # for x, y in test_set:
    #     print("对于测试值：{}，期望值为:{}\t实际值为:{}".format(x, y, sol.trap(x)))
    test_stack = [1, 2, 3, 4, 5]
    print(test_stack)
    test_stack.pop()
    print(test_stack)
