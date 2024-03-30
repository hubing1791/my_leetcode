# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
from typing import List


class Solution:
	# 动态规划法。具体见官方题解
	def findLength_dp(self, nums1: List[int], nums2: List[int]) -> int:
		n, m = len(nums1), len(nums2)
		result = 0
		# 要乘以m+1是因为，这个是从后往前倒推的，看下题解就都明白了
		dp = [[0] * (m + 1) for i in range(n + 1)]
		for i in range(n - 1, -1, -1):
			for j in range(m - 1, -1, -1):
				if nums1[i] == nums2[j]:
					dp[i][j] = 1 + dp[i + 1][j + 1]
					result = max(result, dp[i][j])
		return result

	# 滑动窗口法，实际上就是错位对齐
	def findLength_win(self, nums1: List[int], nums2: List[int]) -> int:
		result = 0
		length1, length2 = len(nums1), len(nums2)
		# length1应该加在nums1的下标上，相当于nums2右移对其了
		for i in range(0, length1 - 1):
			max_index = min(length1 - i, length2)
			k = 0
			for j in range(max_index):
				if nums1[i + j] == nums2[j]:
					k += 1
					result = max(result, k)
				else:
					k = 0
		for i in range(1, length2 - 1):
			max_index = min(length2 - i, length1)
			k = 0
			for j in range(max_index):
				if nums1[j] == nums2[j+i]:
					k += 1
					result = max(result, k)
				else:
					k = 0
		return result
