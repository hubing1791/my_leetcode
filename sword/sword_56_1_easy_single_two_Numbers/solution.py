# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
# 2022-05-05
from typing import List


class Solution:
	# 这样写麻烦了
	def singleNumbers(self, nums: List[int]) -> List[int]:
		x = nums[0]
		for x_ in nums[1:]:
			x ^= x_
		digit_num = 0
		while x >> digit_num & 1 != 1:
			digit_num += 1
		left, right = 0, len(nums) - 1
		while left < right:
			while left < right and nums[right] >> digit_num & 1 == 1:
				right -= 1
			while left < right and nums[left] >> digit_num & 1 == 0:
				left += 1
			nums[right], nums[left] = nums[left], nums[right]
		a, b = nums[0], nums[right + 1]
		for a_ in nums[1:right + 1]:
			a ^= a_
		for b_ in nums[right + 2:]:
			b ^= b_
		return [a, b]

	# 我的代码的改进版,然而可以继续改进，根本没必要先分组，直接根据不同情况抑或即可
	def singleNumbers_new(self, nums: List[int]) -> List[int]:
		x = nums[0]
		for x_ in nums[1:]:
			x ^= x_
		div = 1
		# 这种情况下，最终x&div为2^n
		while div & x == 0:
			div = div << 1
		left, right = 0, len(nums) - 1
		# print(x,div,x&div)
		while left < right:
			while left < right and nums[right] & div !=0:
				right -= 1
			while left < right and nums[left] & div == 0:
				left += 1
			nums[right], nums[left] = nums[left], nums[right]
		a, b = nums[0], nums[right + 1]
		for a_ in nums[1:right + 1]:
			a ^= a_
		for b_ in nums[right + 2:]:
			b ^= b_
		return [a, b]

	# 继续改进
	def singleNumbers_new1(self, nums: List[int]) -> List[int]:
		x = nums[0]
		for num in nums[1:]:
			x ^= num
		div = 1
		# 这种情况下，最终x&div为2^n
		while div & x == 0:
			div = div << 1
		a,b = 0,0
		for num in nums:
			if num &div == 0:
				a^=num
			else:
				b^=num
		return [a,b]



if __name__ == '__main__':
	so = Solution()
	so.singleNumbers_new([1, 2, 5, 2])
