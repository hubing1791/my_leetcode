# https://leetcode-cn.com/problems/wildcard-matching/
# 2022-03-03

class Solution:
	def isMatch_dp(self, s: str, p: str) -> bool:
		s_length, p_length = len(s), len(p)
		# 状态转移是需要-1，因此需要在长度上加一才能完整的动态规划
		dp_matrix = [[False] * (s_length + 1) for _ in range(p_length + 1)]
		dp_matrix[0][0] = True
		# [0][x]为true当且仅当p的前X个字符全部是*
		for i in range(1, p_length + 1):
			if p[i - 1] == '*':
				dp_matrix[0][i] = True
			else:
				break

		# 处理dp,注意要从1开始
		for i in range(1, s_length + 1):
			for j in range(1, p_length + 1):
				# j是第j个字符，对应下标需要减一
				if p[j - 1] == '*':
					dp_matrix[j][i] = dp_matrix[j - 1][i] | dp_matrix[j][i - 1]
				elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
					dp_matrix[j][i] = dp_matrix[j - 1][i - 1]

		return dp_matrix[-1][-1]

	def isMatch_greedy(self, s: str, p: str) -> bool:
		# 首先解决结尾不是*的情况
		s_length, p_length = len(s), len(p)
		# 此时s_length就表示了最终需要遍历到的最右边的位置而不是指长度，需要注意。p_length类似
		while p_length > 0 and p[p_length - 1] != '*' and s_length > 0:
			if p[p_length - 1] == s[s_length - 1] or p[p_length - 1] == '?':
				s_length -= 1
				p_length -= 1
			else:
				return False
		# 如果此时已经把模式字符串走光了，那么s也必须走光
		if p_length == 0:
			return s_length == 0

		# 开始从左向右的匹配
		s_index, p_index, s_record, p_record = 0, 0, -1, -1
		while s_index < s_length and p_index < p_length:
			# 是*号意味着记录点可以右移
			if p[p_index] == '*':
				p_index += 1
				s_record, p_record = s_index, p_index
			# 匹配到了一般情况两个字符串都右移
			elif p[p_index] == s[s_index] or p[p_index] == '?':
				s_index += 1
				p_index += 1
			# 如果匹配失败，可以在s上移动，前提是s之前匹配到了*，也就是srecord已经不是-1
			elif s_record != -1 and s_record + 1 < s_length:
				s_record += 1
				s_index, p_index = s_record, p_record
			else:
				return False
		# 经过上面的匹配，至少有一个走完了，p结尾是*，因此s没走完无所谓。而若是p没走完，那p的结尾必须全是*
		for i in range(p_index, p_length):
			if p[i] != '*':
				return False
		return True
