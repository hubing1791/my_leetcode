# https://leetcode-cn.com/problems/decode-ways/
# 2021-10-01

class Solution:
	# 遇到特殊情况复杂度会爆炸，比如一直在分叉的
	def numDecodings(self, s: str) -> int:
		code_set = set()
		for i in range(1, 27):
			code_set.add(str(i))

		# 编码的长度上限显然为字符串的长度
		length_limit: int = len(s)
		count_codes = 0

		# 传入当前编码到达的位置
		def codeDFS(a: int):
			nonlocal count_codes
			if a >= length_limit:
				count_codes += 1
				return 0
			if s[a:a + 1] in code_set:
				codeDFS(a + 1)
			if a + 2 <= length_limit and s[a:a + 2] in code_set:
				codeDFS(a + 2)
			return 0

		codeDFS(0)
		return count_codes

	# 用动态规划实现
	# 一开始没考虑解码方案不存在的情况，错了很多次
	def numDecodingsDP(self, s: str) -> int:
		code_set = set()
		for i in range(1, 27):
			code_set.add(str(i))
		length = len(s)
		count_codes = 0
		if length == 1 and s not in code_set:
			return 0
		elif length == 1:
			return 1
		# step0，step1分别表示1位前的组合数和0位前的组合数
		step0 = 1
		step1 = 1 if s[0] in code_set else 0
		for i in range(1, length):
			step_temp = 0
			if s[i] in code_set:
				step_temp += step1
			if s[i - 1:i + 1] in code_set:
				step_temp += step0
			step0 = step1
			step1 = step_temp
		return step1

if __name__ == "__main__":
	sol = Solution()
	print(sol.numDecodings("111111111111111111111111111111111111111111111"))
