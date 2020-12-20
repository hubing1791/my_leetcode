# 特殊输入有‘ ’，‘hello’(这种情况在索引倒回去的时候可能会出界)
# 这个写法巨慢

class Solution:
    def lengthOfLastWord(self, s):
        length_str = len(s)
        if '' == s:  # 改成if not s更快
            return 0
        i, j = -1, 0
        while abs(i) <= length_str and s[i] == ' ':  # s.strip(' ')比我这样写更快
            i -= 1
        while abs(i) <= length_str and s[i] != ' ':
            j += 1
            i -= 1
        return j


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))
