class Solution:
	# 尝试下双指针加有限状态自动机实现
	# 第一版无法处理a*a，a*...这种，不对
	def isMatch(self, s: str, p: str) -> bool:
		if s == '':
			return False
		elif p == '':
			return True
		else:
			pass
		pointer_s, pointer_p, s_boundary, p_boundary = 0, 0, len(s) - 1, len(p) - 1
		while pointer_s <= s_boundary and pointer_p <= p_boundary:
			temp_char = p[pointer_p]
			if pointer_p < p_boundary and p[pointer_p + 1] == '*':
				pointer_p += 2
				if temp_char != '.':
					while pointer_s <= s_boundary and temp_char == s[pointer_s]:
						pointer_s += 1
				else:
					pointer_s = s_boundary + 1
			else:
				pointer_p += 1
				if temp_char != '.':
					if temp_char == s[pointer_s]:
						pointer_s += 1
					else:
						return False
				else:
					pointer_s += 1
		if pointer_s == s_boundary + 1 and pointer_p == p_boundary + 1:
			return True
		else:
			return False

	def isMatch2(self, s: str, p: str) -> bool:
		def match(i, j):
			if i == 0:
				return False
			elif p[j - 1] == '.':
				return True
			else:
				return s[i - 1] == p[j - 1]

		dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
		dp[0][0] = True
		for i in range(len(s) + 1):
			for j in range(1, len(p) + 1):
				if p[j - 1] == '*':
					dp[i][j] |= dp[i][j - 2]
					if match(i, j - 1):
						dp[i][j] |= dp[i - 1][j]
				else:
					if match(i, j):
						dp[i][j] |= dp[i - 1][j - 1]
		return dp[len(s)][len(p)]


if __name__ == '__main__':
	testlist = [['aa', 'a'], ['aaa', 'a*'], ['abcdefghijklmn', '.*'], ['aab', 'c*a*b'], ['mississippi', 'mis*is*p*']]
	sol = Solution()
	for x, y in testlist:
		print(sol.isMatch(x, y))
