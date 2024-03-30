# https://leetcode-cn.com/problems/rotate-matrix-lcci/
# 2022-05-08
from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		l, r = 0, len(nums)-1
		while 0 <= l <= r < len(nums):
			m = (l + r) // 2
			if target < nums[m]:
				r = m - 1
			elif target > nums[m]:
				l = m + 1
			else:
				return m
		return -1


if __name__ == '__main__':
	so = Solution()
	so.search([-1, 0, 3, 5, 9, 12], 9)
