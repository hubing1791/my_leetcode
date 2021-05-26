# 偷懒版，利用了python自带的函数
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a, 2) + int(b, 2)
        c = str(bin(c))
        return c[2:]


if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary('11', '1'))
