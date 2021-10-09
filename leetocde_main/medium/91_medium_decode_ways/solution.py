# https://leetcode-cn.com/problems/decode-ways/
# 2021-10-01

class Solution:
    def numDecodings(self, s: str) -> int:
        code_set = set()
        for i in range(1, 27):
            code_set.add(str(i))

        # 编码的长度上限显然为字符串的长度
        length_limit: int = len(s)
        count_codes = 0
        # 传入当前编码到达的位置
        def codeDFS(a: int):
            nonlocal count_codes
            if a >= length_limit:
                count_codes += 1
                return 0
            if s[a:a + 1] in code_set:
                codeDFS(a + 1)
            if a + 2 <= length_limit and s[a:a + 2] in code_set:
                codeDFS(a + 2)
            return 0

        codeDFS(0)
        return count_codes


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("12"))
