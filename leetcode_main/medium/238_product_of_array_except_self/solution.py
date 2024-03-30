# https://leetcode-cn.com/problems/product-of-array-except-self/
from typing import List


class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		length = len(nums)
		result = [1] * length
		# 用这个数储存暂时的乘积
		tem_num = 1
		for i in range(length):
			result[i] = result[i] * tem_num
			tem_num *= nums[i]
		# 第一这样乘完后，位置i的数字缺了位置i之后的乘积，倒着往回一次就行了
		print(result)
		tem_num = 1
		for i in range(-1, -length - 1, -1):
			result[i] = result[i] * tem_num
			tem_num *= nums[i]
		return result


if __name__ == "__main__":
	sol = Solution()
	sol.productExceptSelf([1, 2, 3, 4])
