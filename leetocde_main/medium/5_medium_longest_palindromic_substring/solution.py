class Solution:
    # 官方解答第一种，动态规划,速度一坨屎，比第二种中心扩散慢了9倍
    def longestPalindrome(self, s: str) -> str:
        length_s = len(s)
        dp = [[False]*length_s for i in range(length_s)]  # 状态转移矩阵
        result = ''
        for m in range(length_s):
            for i in range(length_s):
                j = i + m
                if j >= length_s:
                    break
                if not m:
                    dp[i][j] = True
                elif m == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and m + 1 > len(result):
                    result = s[i:j + 1]
        return result
