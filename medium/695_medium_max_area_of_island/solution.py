# https://leetcode-cn.com/problems/max-area-of-island/

from typing import List


class Solution:
    # 写的不对，无法处理格子计数，使用的加左上方的策略
    # 直接在grid上操作，制作第二版dp，取过的位置置为0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        width, length = len(grid), len(grid[0])
        dp = [[0] * length for i in range(width)]
        result = 0
        # 只加上面的和左边的，第一排和第一列比较特殊直接拿出来处理
        dp[0][0] = grid[0][0]
        for j in range(1, length):
            if dp[0][j]:
                dp[0][j] = dp[0][j - 1] + grid[0][j]
                result = max(result, dp[0][j])
        for i in range(1, width):
            if dp[i][0]:
                dp[i][0] = dp[i - 1][0] + grid[i][0]
                result = max(result, dp[i][0])
        for i in range(1, width):
            for j in range(1, length):
                # 只有对应格子有值才继续累加
                if dp[i][j]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + grid[i][j]
                    result = max(result, dp[i][0])
        return result

    # 无法正确计算右下角有缺口的情况
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        width, length = len(grid), len(grid[0])
        result = 0
        for i in range(1, width):
            for j in range(1, length):
                if grid[i][j]:
                    if i > 0 and j > 0:
                        grid[i][j] = 1 + grid[i - 1][j] + grid[i][j - 1]
                        result = max(result, grid[i][j])
                        grid[i - 1][j] = grid[i][j - 1] = 0
                    elif not i and j:
                        grid[i][j] = 1 + grid[i][j - 1]
                        result = max(result, grid[i][j])
                        grid[i][j - 1] = 0
                    elif i and not j:
                        grid[i][j] = 1 + grid[i - 1][j]
                        result = max(result, grid[i][j])
                        grid[i - 1][j] = 0
                    else:
                        pass
        return result

    # 看解答写
    def maxAreaOfIsland3(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        width, length = len(grid), len(grid[0])
        stack = []
        result = 0
        for i in range(width):
            for j in range(length):
                stack.append((i, j))
                cur = 0  # 这一轮计算中的岛屿面积
                while stack:
                    cur_i, cur_j = stack.pop()
                    if cur_i < 0 or cur_j < 0 or cur_i >= width or cur_j >= length or grid[cur_i][cur_j] == 0:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    result = max(cur, result)
                    for x, y in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                        stack.append((cur_i + x, cur_j + y))
        return result
