# https://leetcode-cn.com/problems/generate-parentheses/
from typing import List


class Solution:
    # 深度优先搜索
    def generateParenthesis(self, n: int) -> List[str]:
        def parenthesis(left: int, right: int, s: str, n):
            if left == right == n:
                result.append(s)
                return 0
            if left < n:
                parenthesis(left + 1, right, s + '(', n)
            if right < left:
                parenthesis(left, right + 1, s + ')', n)

        result = []
        parenthesis(0, 0, '', n)
        return result
