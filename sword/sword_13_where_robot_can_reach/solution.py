# https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/

class Solution:
    # 自己写的递归方法，对的但是很慢
    def movingCount(self, m: int, n: int, k: int) -> int:
        result = 0
        # 构造一个数列记录这个点上去过没有
        map_valid = [[1] * n for i in range(m)]

        # 构造一个各位之和的辅助函数
        def add_digit(num: int):
            result_add = 0
            while num > 0:
                result_add += num % 10
                num //= 10
            return result_add

        def helper(x: int, y: int):
            nonlocal result
            if(add_digit(x) + add_digit(y)) <= k:
                result += 1
                map_valid[x][y] = 0
                # 注释掉的是我的版本，其实不用向左和向上搜索
                # for x1, y1 in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                for x1, y1 in [[1, 0], [0, 1]]:
                    if m > (x + x1) > -1 and n > (y + y1) > -1 and map_valid[x + x1][y + y1] == 1:
                        helper(x + x1, y + y1)

        helper(0, 0)
        return result
