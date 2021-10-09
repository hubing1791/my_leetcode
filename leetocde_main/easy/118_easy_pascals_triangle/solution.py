# https://leetcode-cn.com/problems/pascals-triangle/
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows + 1):
            temp_layer = [1] * i
            if i == 1 or i == 2:
                result.append(temp_layer)
            else:
                for j in range(1, i - 1):
                    temp_layer[j] = result[-1][j - 1] + result[-1][j]
                result.append(temp_layer)
        return result
