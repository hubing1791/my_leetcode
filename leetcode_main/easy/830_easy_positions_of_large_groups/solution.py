# https://leetcode-cn.com/problems/positions-of-large-groups/
# 很简单，只是因为每日一题才做的,但是也是有点边界条件要处理

from typing import List


class Solution:
	def largeGroupPositions(self, s: str) -> List[List[int]]:
		result = []
		if not s:
			return result
		temp_char = s[0]
		nums = 1
		for i in range(1, len(s)):
			if temp_char == s[i]:
				nums += 1
			else:
				if nums >= 3:
					result.append([i - nums, i - 1])
				nums = 1
				temp_char = s[i]
		# 这个一开始没想到
		if nums >=3:
			result.append([len(s)-nums,len(s)-1])
		return result


if __name__ == '__main__':
	test_set = [
		["abbxxxxzzy", [3, 6]]
	]
	sol = Solution()
	for x, y in test_set:
		print(str(sol.largeGroupPositions(x)) + '\t' + str(y))
