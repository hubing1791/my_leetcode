# https://leetcode-cn.com/problems/add-digits/
# 2022-03-03

class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0
