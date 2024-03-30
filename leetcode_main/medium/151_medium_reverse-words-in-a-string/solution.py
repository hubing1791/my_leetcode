# https://leetcode.cn/problems/reverse-words-in-a-string/
# 2024-03-30

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = [x for x in s.split(" ") if x != ""]
        s_list.reverse()
        return " ".join(s_list)
        