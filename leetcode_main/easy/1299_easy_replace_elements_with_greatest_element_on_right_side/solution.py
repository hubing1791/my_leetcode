# https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side/
from typing import List


class Solution:
	def replaceElements(self, arr: List[int]) -> List[int]:
		length = len(arr)
		temp_max = arr[-1]
		arr[-1] = -1
		for i in range(-2, -length - 1, -1):
			temp = arr[i]
			arr[i] = temp_max
			if temp > temp_max:
				temp_max = temp
		return arr
