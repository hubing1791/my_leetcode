# https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
# 2022-05-06
import math
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        result = []
        n_max = int(math.sqrt(target * 2))
        for i in range(n_max, 1, -1):
            a = (target - ((i - 1) * i) / 2) / i
            if a == int(a):
                temp_result = [int(a)] * i
                for j in range(i):
                    temp_result[j] += j
                result.append(temp_result)
        return result


if __name__ == '__main__':
    print(int(1.0) == 1.0)
