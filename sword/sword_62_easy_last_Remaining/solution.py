# https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
# 2022-05-06

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f