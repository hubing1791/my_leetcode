# https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
from typing import List


class Solution:
	def isStraight(self, nums: List[int]) -> bool:
		nums.sort()
		king = 0  # 大小王数量
		temp = 0
		for i in range(0, len(nums)):
			if nums[i] == 0:
				king += 1
			elif i == 0 or nums[i - 1] == 0:
				temp = nums[i]
			else:
				if nums[i] > temp + 1:
					if king:
						# 差值是3的时候只需要补充2张牌
						distance = nums[i] - temp - 1
						if distance > king:
							return False
						else:
							king -= distance
							temp = nums[i]
					else:
						return False
				elif nums[i] == temp + 1:
					temp += 1
				else:
					return False
		return True
