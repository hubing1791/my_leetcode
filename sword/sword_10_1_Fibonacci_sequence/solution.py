# https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        f0 = 0
        f1 = 1
        for i in range(1, n):
            print(i)
            f_temp = f1
            f1 += f0
            f0 = f_temp
            if i % 10 == 0:
                f0, f1 = f0 % 1000000007, f1 % 1000000007
        return f1 % 1000000007


if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(2))
