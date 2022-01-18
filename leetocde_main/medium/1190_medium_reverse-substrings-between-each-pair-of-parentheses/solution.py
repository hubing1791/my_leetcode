# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# 2021-12-16

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i, char_temp in enumerate(s):
            if char_temp == ')':
                s_temp = ''
                char_reverse = stack.pop()
                while char_reverse != '(':
                    s_temp += char_reverse
                    char_reverse = stack.pop()
                for char_reverse_temp in s_temp:
                    stack.append(char_reverse_temp)
                # if stack:
                #     for char_reverse_temp in s_temp:
                #         stack.append(char_reverse_temp)
                # else:
                # 可能是（xxx）xxx这种，这样的写法解决不了（xxx）xxx（xx）这种
                # return s_temp + s[i+1:]
            else:
                stack.append(char_temp)
        return ''.join(stack)

    def reverseParenthesesofficial2(self, s: str) -> str:
