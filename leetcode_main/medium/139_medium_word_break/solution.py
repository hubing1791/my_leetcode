# https://leetcode-cn.com/problems/word-break/
from typing import List


class Solution:
	# 这个写法无法照顾可能的不同组合，例如给了cars ，字典是[car,ca,rs]
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		length_list = []
		for i in wordDict:
			if len(i) not in length_list:
				length_list.append(len(i))
		cycle_number = 0  # 初始循环位置
		while cycle_number < len(s):
			for i in length_list:
				if s[cycle_number:cycle_number + i] in wordDict:
					cycle_number += i
					break
			else:
				return False
		return True

	# 对的，但是超时
	def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
		length_list = []
		for i in wordDict:
			if len(i) not in length_list:
				length_list.append(len(i))

		def helper(index: int):
			if index == len(s):
				return True
			result = False
			for i in length_list:
				if s[index:index + i] in wordDict:
					result |= helper(index + i)
			return result

		return helper(0)

	def wordBreakdp(self, s: str, wordDict: List[str]) -> bool:
		n = len(s)
		dp = [False] * (n + 1)
		dp[0] = True
		for i in range(n):
			for j in range(i + 1, n + 1):
				dp[j] |= dp[i] if s[i:j] in wordDict else False
		return dp[-1]
