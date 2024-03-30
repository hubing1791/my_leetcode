# https://leetcode-cn.com/problems/combination-sum/
from typing import List


class Solution:
	# 自己尝试实现，原理是不停递归，还差多大的数字，如果可以找到就往结果里添加,
	# 但是速度很慢，之后改进了一下，先把candidates排序，之后比较时可以减少比较次数,但还是很慢
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		def findnum(temp_result: List[int], num_remain: int):
			for i in candidates:
				if i <= num_remain:
					result_cycle = temp_result.copy()
					result_cycle.append(i)
					if not num_remain - i:
						results.append(result_cycle)
					else:
						findnum(result_cycle, num_remain - i)
				else:
					break

		results = []
		candidates.sort()
		findnum([], target)
		for i in results:
			i.sort()
		results_true = []
		for i in results:
			if i not in results_true:
				results_true.append(i)
		return results_true

	# 看了别人的解答，总体思路不变，但是提供了避免重复的办法，并且避免重复后也就不需要像我那样使用copy和去重了,
	# 在递归函数中加入
	def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
		def findnum(index_start, temp_result, num_remain):
			for i in range(index_start, n):
				if candidates[i] < num_remain:
					findnum(i, temp_result + [candidates[i]], num_remain - candidates[i])
				elif candidates[i] == num_remain:
					results.append(temp_result + [candidates[i]])
				else:
					break

		results = []
		n = len(candidates)
		candidates.sort()
		findnum(0, [], target)
		return results


if __name__ == '__main__':
	sol = Solution()
	test_set = [[[2, 3, 6, 7], 7],
				[[2, 3, 5], 8],
				]
	for x, y in test_set:
		print(sol.combinationSum1(x, y))
	# res =[1,2]
	# res1 = res
	# res1.append(3)
	# print(res)
