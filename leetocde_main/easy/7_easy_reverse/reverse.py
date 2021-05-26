class Solution:
    def reverse(self, x: int) -> int:
        res, abs_num = 0, abs(x)
        if x > 0:
            boundry = (1 << 31) - 1
        else:
            boundry = 1 << 31
        while abs_num != 0:
            res = res * 10 + abs_num % 10
            if res > boundry:
                return 0
            abs_num //= 10
        if x > 0:
            return res
        else:
            return -res
