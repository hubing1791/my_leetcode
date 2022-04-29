# 动态规划版
class Solution:
    def numWays(self, n: int, relation, k: int) -> int:
        for i in range(k):
            dp = [[0] * n for i in range(k + 1)]
            dp[0][0] = 1
            for i in range(k):
                for x, y in relation:
                    dp[i + 1][y] += dp[i][x]
        return dp[k][n - 1]