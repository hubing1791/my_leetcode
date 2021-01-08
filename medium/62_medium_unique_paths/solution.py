# https://leetcode-cn.com/problems/unique-paths/
class Solution:
    # 上来觉得可以利用动态规划加递归，但是转念一想好像没必要，直接扫描好像就可以了
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i and j:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif not i and not j:
                    dp[i][j] = 1
                elif not i:
                    dp[i][j] += dp[i][j - 1]
                else:
                    dp[i][j] += dp[i - 1][j]
        return dp[-1][-1]
