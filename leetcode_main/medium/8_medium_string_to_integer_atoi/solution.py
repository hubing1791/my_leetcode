# https://leetcode-cn.com/problems/string-to-integer-atoi/
# 看了题解，有限状态自动机会比大量的if好。

MAX_INT = 2 ** 31 - 1
MIN_INT = 2 ** 31


class Automato:
    def __init__(self):
        # 标志位，默认为 1
        self.sign = 1
        self.state = "start"
        self.ans = 0
        # 这个表表示遇到了空格，+/-，数字,其它字符对应的状态变化
        self.table = {
            "start": ["start", "signed", "number", "end"],
            "signed": ["end", "end", "number", "end"],
            "number": ["end", "end", "number", "end"],
            "end": ["end", "end", "end", "end"]
        }

    # 将符号转换为下标
    def trans(self, a):
        if a == ' ':
            return 0
        elif a == '+' or a == '-':
            return 1
        elif a.isdigit():
            return 2
        else:
            return 3

    def getchar(self, a):
        self.state = self.table[self.state][self.trans(a)]
        if self.state == "number":
            self.ans = self.ans * 10 + int(a)
            self.ans = min(self.ans, MAX_INT) if self.sign == 1 else min(self.ans, MIN_INT)
        elif self.state == "signed":
            if a == "-":
                self.sign = -1


class Solution:

    def myAtoi(self, s: str) -> int:
        autom = Automato()
        for i in s:
            autom.getchar(i)
        return autom.sign * autom.ans


if __name__ == "__main__":
    test_set = ["42", "[", "-9999999999999999999999", ]
    sol = Solution()
    for i in test_set:
        print(sol.myAtoi(i))
