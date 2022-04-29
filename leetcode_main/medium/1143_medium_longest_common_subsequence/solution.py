# https://leetcode-cn.com/problems/longest-common-subsequence/
# 参考题解 https://leetcode-cn.com/problems/longest-common-subsequence/solution/dong-tai-gui-hua-zhi-zui-chang-gong-gong-zi-xu-lie/

class Solution:
    # 这个会超时
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 从后往前递归循环
        def helper(i, j):
            # 已经循环到头
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                # 相等则都往前进
                return helper(i - 1, j - 1) + 1
            else:
                # 不相等选一个前进，并且选择更大的
                return max(helper(i - 1, j), helper(i, j - 1))

        return helper(len(text1) - 1, len(text2) - 1)

    # 非递归方法
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]
