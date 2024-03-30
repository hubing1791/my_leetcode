# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
# 2022-05-03

from collections import defaultdict


class Solution:
	def translateNum(self, num: int) -> int:
		num_english = defaultdict(lambda: '?')
		for i in range(26):
			num_english[str(i)] = chr(i + 97)
		num_str = str(num)
		index_max = len(num_str) - 1
		result = 0

		def DFS(index: int):
			nonlocal num_str
			nonlocal index_max
			nonlocal result
			if index > index_max:
				result += 1
				return
			# 其实只进一位根本没必要比
			if num_english[num_str[index]] != '?':
				DFS(index + 1)
			if index + 1 <= index_max and num_english[num_str[index:index+2]] != '?':
				DFS(index + 2)
		DFS(0)
		return result


if __name__ == '__main__':
	so = Solution()
	print(so.translateNum(1))
