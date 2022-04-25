import re


class Solution:
    def replaceSpace(self, s: str) -> str:
        s_ = re.sub("[ ]", "%20", s)
        return s_


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceSpace(" you are my f"))
