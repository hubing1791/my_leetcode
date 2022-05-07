# https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
# 2022-05-06

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]