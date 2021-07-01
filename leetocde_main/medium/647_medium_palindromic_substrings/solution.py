# https://leetcode-cn.com/problems/palindromic-substrings/

class Solution:
    # 动态规划
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        dp = [[0] * length for i in range(length)]
        result = 0
        for i in range(length):
            dp[i][i] = 1
            j = 1
            while i - j >= 0 and i + j < length:
                dp[i - j][i + j] = dp[i - j + 1][i + j - 1] and s[i - j] == s[i + j]
                j += 1
        for i in range(length - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            j = 1
            while i - j >= 0 and i + j + 1 < length:
                dp[i - j][i + j + 1] = dp[i - j + 1][i + j] and s[i - j] == s[i + j + 1]
                j += 1
        # for i in range(length):
        #     for j in range(length):
        #         if dp[i][j]:
        #             result +=1
        # # 剔除重复计数的，dp[1][2],dp[2][1]是对称的
        # # 上述计数方法有问题，因为在第二波动态规划中，dp[4][3]这样的值不会被照顾到
        # result = (result+length)//2
        for i in range(length):
            for j in range(i, length):
                if dp[i][j]:
                    result += 1
        return result

    # 把上面的写的简洁一些
    def countSubstrings_1(self, s: str) -> int:
        length = len(s)
        dp = [[0] * length for i in range(length)]
        result = 0
        # 为什么可以直接用到length -1，是因为最后一个数作为中心时，必然只有一种情况那就是最后一个字符自己作为子串，因此可以把两次放在一起
        for i in range(length - 1):
            dp[i][i] = 1
            dp[i][i + 1] = s[i] == s[i + 1]
            j = 1
            while i - j >= 0:
                if i + j < length:
                    dp[i - j][i + j] = dp[i - j + 1][i + j - 1] and s[i - j] == s[i + j]
                if i + j + 1 < length:
                    dp[i - j][i + j + 1] = dp[i - j + 1][i + j] and s[i - j] == s[i + j + 1]
                j += 1
        for i in range(length):
            for j in range(i, length):
                if dp[i][j]:
                    result += 1
        # 少数了一个
        return result + 1


if __name__ == "__main__":
    test_set = [
        'aaa'
    ]
    sol = Solution()
