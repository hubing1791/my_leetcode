# https://leetcode-cn.com/problems/restore-ip-addresses/
from typing import List


class Solution:
	# 写一半不想写了，逻辑铁对但是具体实现细节写的很麻烦
	def restoreIpAddresses(self, s: str) -> List[str]:
		length = len(s)
		result = []

		# 三个参数依次表示为轮数，目前已经拼接出的字符串，目前到达的下标的数
		def dfs_ip(round_ip: int, str_up_tp_now: str, index_now: int):
			nonlocal length
			nonlocal result
			# 先把字符串过长或者过短排除
			if (5 - round_ip) > length - index_now or (5 - round_ip) * 3 < length - index_now:
				return
			if round_ip == 4:
				pass
			if length - index_now >= 1:
				pass

	# 官方题解
	def restoreIpAddresses_offical(self, s: str) -> List[str]:
		temp_seg = [0] * 4
		result = []
		length = len(s)

		# 参数分别为轮数，指向的下标
		def dfs(round_id: int, index: int):
			if round_id == 4:
				if index == length:
					result.append('.'.join(str(seg) for seg in temp_seg))
				return
			else:
				# 没用完就到了
				if index == length:
					return
					# 前缀第一个是零则必须在此位置为零
				if s[index] == '0':
					temp_seg[round_id] = 0
					dfs(round_id + 1, index + 1)
				# 一般情况
				num = 0
				for i in range(index, length):
					num = num * 10 + int(s[i])
					if 0 < num < 256:
						temp_seg[round_id] = num
						dfs(round_id + 1, i + 1)
					else:
						break
		dfs(0,0)
		return result