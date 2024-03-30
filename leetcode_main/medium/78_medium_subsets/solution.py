# https://leetcode-cn.com/problems/subsets/
from typing import List


class Solution:
	# 想到了01编码，果然答案也这么想的，这是递归版本
	def subsets(self, nums: List[int]) -> List[List[int]]:
		# 传递已经生成的子集，已经到达的位置，下一个位置取不取
		def helper(nums_subset: List[int], location: int):
			if location == length_nums:
				result.append(nums_subset)
			else:
				nums_subset1 = nums_subset.copy()
				nums_subset2 = nums_subset.copy()
				nums_subset2.append(nums[location])
				helper(nums_subset1, location + 1)
				helper(nums_subset2, location + 1)

		length_nums = len(nums)
		result = []
		helper(result, 0)
		return result

	# 抄的迭代版本，巨牛逼
	def subsets(self, nums: List[int]) -> List[List[int]]:
		res = [[]]
		for i in nums:
			res = res + [[i] + num for num in res]
		return res


if __name__ == '__main__':
	test_set = [
		[1, 2, 3]
	]
	sol = Solution()
	for x in test_set:
		print(sol.subsets(x))
