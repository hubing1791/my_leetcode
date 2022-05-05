# https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
# 2022-05-05
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        char_dict = {}
        for char in s:
            char_dict[char] = char not in char_dict
        for k, v in char_dict.items():
            if v:
                return k
        return ' '
