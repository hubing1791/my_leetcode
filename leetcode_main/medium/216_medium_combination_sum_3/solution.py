# https://leetcode-cn.com/problems/combination-sum-iii/
# 2021-12-16

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        # 已经有的序列,剩余次数，剩余数字
        def helper(list_temp: List, count_left: int, num_left: int):
            if not list_temp:
                # 没有必要数到num_left
                # 一开始这儿没有min，会导致出现大于9的数字
                for i in range(1, min(num_left - count_left, 10)):
                    helper(list_temp + [i], count_left - 1, num_left - i)
            else:
                if count_left > 1:
                    for i in range(list_temp[-1] + 1, min(num_left - count_left, 10)):
                        helper(list_temp + [i], count_left - 1, num_left - i)
                else:
                    # 限制最后剩余数字的大小
                    if list_temp[-1] < num_left < 10:
                        result.append(list_temp + [count_left])
                    return

        helper([], k, n)
        return result


if __name__ == "__main__":
    sol = Solution()
    test_set = [
        [3, 7]
    ]
    for k, n in test_set:
        sol.combinationSum3(k, n)
