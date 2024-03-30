# https://leetcode-cn.com/problems/check-permutation-lcci/
# 2022-05-07
from collections import defaultdict


class Solution:
	# 重排看是否相等
	def CheckPermutation(self, s1: str, s2: str) -> bool:
		s1_list = list(s1)
		s1_list.sort()
		s2_list = list(s2)
		s2_list.sort()
		return s1_list == s2_list

	# 用hash表判断(其实就是在计数)
	def CheckPermutation2(self, s1: str, s2: str) -> bool:
		s1_list, s2_list = [0] * 26, [0] * 26
		for char in s1:
			s1_list[ord(char) - ord('a')] += 1
		for char in s2:
			s2_list[ord(char) - ord('a')] += 1
		return s1_list == s2_list


if __name__ == '__main__':
	test_set = [
		["abc", "bad"]
	]
	so = Solution()
	for s1, s2 in test_set:
		so.CheckPermutation(s1, s2)
