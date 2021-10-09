# https://leetcode-cn.com/problems/set-matrix-zeroes/
# 2021-09-17
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 记录某个位置是否需要置为零的数组
        need_zero = [False] * (len(matrix) + len(matrix[0]))
