# https://leetcode-cn.com/problems/palindrome-permutation-lcci/
# 2022-05-07

from collections import defaultdict


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
        count_odd = 0
        for v in char_dict.values():
            if v % 2 == 1:
                count_odd += 1
                # 把判断移动到if下会加快，一开始这个if和上一个平行
                if count_odd > 1:
                    return False
        return True

    # 用位上的结果表示有没有
    def canPermutePalindrome1(self, s: str) -> bool:
        result = 0
        for c in s:
            result ^= 1 << ord(c)

        return result & (result - 1) == 0
