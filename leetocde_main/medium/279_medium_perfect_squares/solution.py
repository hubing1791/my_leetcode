# https://leetcode-cn.com/problems/perfect-squares/


class Solution:
    # 暴力加剪枝，其实复杂度不比动态规划差
    def numSquares(self, n: int) -> int:
        # 最大也就是n个1，所以这样初始化
        max_time = n

        # 参数依次代表着尝试次数，剩下的可用的最大的数（因为要使得结果有序的被尝试出，不停去掉可以尝试使用的最大数），剩余的值
        def recur(try_time: int, try_num_max: int, num_left: int):
            nonlocal max_time
            for i in range(try_num_max, 0, -1):
                if num_left - i * i > 0:
                    if try_time + 1 >= max_time:
                        # 这里可以直接break，因为i越来越小，之后肯定还会满足超过最大次数的条件，不如早点结束循环
                        break
                    else:
                        recur(try_time + 1, i, num_left - i * i)
                elif num_left - i * i == 0:
                    max_time = min(max_time, try_time + 1)
                else:
                    pass

        sqrt_num = 1
        for i in range(1, n):
            if i * i > n:
                sqrt_num = i - 1
        recur(0, sqrt_num, n)
        return max_time

    # 动态规划版
    # https://leetcode-cn.com/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode-solut-t99c/
    def numSquares_dyn(self, n: int) -> int:
        # 不可能会得到比n大的结果，且f(0) = 0
        dp_list = [n] * (n + 1)
        dp_list[0] = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if i - j * j >= 0:
                    dp_list[i] = min(dp_list[i], dp_list[i - j * j])
                else:
                    # 不够减及时跳出
                    break
            # 还得加一才是正确值
            dp_list[i] = dp_list[i] + 1
        return dp_list[-1]
