# https://leetcode-cn.com/problems/longest-increasing-subsequence/
from typing import List


class Solution:
	# 写一半想到不对，否了，留着作为反思
	def lengthOfLIS1(self, nums: List[int]) -> int:
		# 记录一个最小值，只有当某个位置的数小于最小值时才有必要向后搜索更新
		# 这样初始化是因为一定从第一个数开始搜索，比第一个数大就可以了
		min_num = nums[0] + 1
		length = len(nums)
		result = 0
		for i in range(length):
			if nums[i] < min_num:
				# temp_max 记录一个当前子序列中最大的值
				temp_max = nums[i]

	# 动态规划,思路是计算以i位置为结尾的序列的最大值
	def lengthOfLIS(self, nums: List[int]) -> int:
		length = len(nums)
		dp = [0] * length
		dp[0] = 1
		# 如果长度只有1那就不会进行扫描了，结果就是1
		result = 1
		for i in range(1, length):
			# 在这一轮就算一个都没匹配到至少值也是1
			max_temp = 1
			for j in range(i):
				if nums[j] < nums[i]:
					max_temp = max(max_temp, dp[j] + 1)
			dp[i] = max_temp
			result = max(max_temp, result)
		return result

	# 贪心+二分
	def lengthOfLIS(self, nums: List[int]) -> int:
		dp = [nums[0]]
		len = 1
		for num in nums:
			if num > dp[-1]:
				dp.append(num)
				len += 1
			else:
				left, right = 0, len - 1
				# location总是根据mid更新向左靠近，因为等于条件和大于放在同一部分
				location = right
				while left <= right:
					mid = (left + right) // 2
					if dp[mid] >= num:
						right = mid - 1
						location = mid
					else:
						left = mid + 1
				dp[location] = num
		return len
