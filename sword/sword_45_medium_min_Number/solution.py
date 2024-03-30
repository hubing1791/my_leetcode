# https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
# 2022-05-02
import functools
from typing import List


class Solution:
	# 这儿先实现利用内置函数的办法，代码比较简单。快排改的先没写
	def minNumber(self, nums: List[int]) -> str:
		def sort_rule(x: str, y: str):
			if int(x + y) < int(y + x):
				return -1
			elif int(x + y) > int(y + x):
				return 1
			else:
				return 0
		nums_str = list(map(str,nums))
		nums_str.sort(key=functools.cmp_to_key(sort_rule))
		return ''.join(nums_str)
