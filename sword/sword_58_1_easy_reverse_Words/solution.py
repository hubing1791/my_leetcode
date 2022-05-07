# https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
# 2022-05-06

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
