# https://leetcode.cn/problems/h-index/
# 2024-02-11

from typing import List

class Solution:
	def hIndex(self, citations: List[int]) -> int:
		# store the num of citation that >= the index of the list
		length = len(citations)
		count_list = [0]*(length+1)
		for x in citations:
			x= length if x>length else x
			count_list[x] +=1
		cum = 0
		for x in range(length,-1,-1):
			cum +=count_list[x]
			if cum>=x:
				return x
		return 0


if __name__ == "__main__":
	test_cases = [
		[3,0,6,1,5]
	]
	sol = Solution()
	for t in test_cases:
		print(sol.hIndex(t))
		
