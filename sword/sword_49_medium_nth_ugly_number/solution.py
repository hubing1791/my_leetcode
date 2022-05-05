# https://leetcode-cn.com/problems/chou-shu-lcof/
# 2022-05-05
from heapq import heapify, heappop, heappush


class Solution:
    def nthUglyNumber_heap(self, n: int) -> int:
        factors = [2, 3, 5]
        heap = [1]
        ugly_set = set([1])

        for _ in range(n - 1):
            cur = heappop(heap)
            for factor in factors:
                if factor * cur not in ugly_set:
                    ugly_set.add(factor * cur)
                    heappush(heap, factor * cur)
        return heappop(heap)

    def nthUglyNumber_dp(self, n: int) -> int:
        dp_list = [0] * n
        dp_list[0] = 1
        # 三个不同的指针
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            # 不能用if elif else，因为可能会出现相等的不止一对的情况
            dp_list[i] = min(dp_list[index2] * 2, dp_list[index3] * 3, dp_list[index5] * 5)
            if dp_list[i] == dp_list[index2] * 2:
                index2 += 1
            if dp_list[i] == dp_list[index3] * 3:
                index3 += 1
            if dp_list[i] == dp_list[index5] * 5:
                index5 += 1
        print(dp_list)
        return dp_list[-1]

if __name__ == '__main__':
    so  = Solution()
    so.nthUglyNumber_dp(10)