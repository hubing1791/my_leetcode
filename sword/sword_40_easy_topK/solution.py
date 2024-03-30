# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
# 2022-05-01
from heapq import heapify, heappop
from typing import List


class Solution:
	def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
		heapify(arr)
		result =[]
		while k>-1:
			result.append(heappop(arr))
		return result
