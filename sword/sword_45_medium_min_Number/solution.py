# https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
# 2022-05-02
from typing import List


class Solution:
    # 这儿先实现利用内置函数的办法，代码比较简单。快排改的先没写
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x:int,y:int):

