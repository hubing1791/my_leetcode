# https://leetcode-cn.com/problems/permutations/
from typing import List


class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		def permute_recursion(nums_remain: set, nums_already):
			for i in nums_remain:
				nums_already_new = [] # 一开始把这个赋值写在了循环外面导致了问题
				if not nums_already:
					nums_already_new.append([i])
				else:
					for t in nums_already:
						nums_already_new.append(t + [i])
				if nums_remain - {i} == set():
					for k in nums_already_new:
						results.append(k)
				else:
					permute_recursion(nums_remain - {i}, nums_already_new)
					# print(nums_already_new)

		results = []
		permute_recursion(set(nums), [])
		return results


if __name__ == '__main__':
	test_set = [
		[1, 2, 3],
		[1, 2, 3, 4]
	]
	sol = Solution()
	for i in test_set:
		print(sol.permute(i))
	# array = set([1])
	# print(array-{1} ==set())
	# # array = set([1, 2, 3, 4])
	# print(array - {1})
	# print(array)
