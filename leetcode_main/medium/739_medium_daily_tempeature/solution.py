# https://leetcode-cn.com/problems/daily-temperatures/
from typing import List


class Solution:
	# 暴力法
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		length = len(temperatures)
		# 温度第一次出现的位置,因为位如下置最大就是length-1，所以可以初始化
		temperature_first = [length] * 71
		result = [length + 1] * length
		for i in range(length - 1, -1, -1):
			# 在第一次出现的温度区域里找
			# 一开始减30了，相当于开始搜索的起点包含了自己
			for j in range(temperatures[i] - 29, 71):
				if temperature_first[j] < length:
					result[i] = min(temperature_first[j] - i, result[i])
			# 更新首次出现位置的信息
			temperature_first[temperatures[i] - 30] = i
			if result[i] == length + 1:
				result[i] = 0
		return result

	# 单调栈
	def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
		stack = []
		length = len(temperatures)
		result = [0] * length
		for i in range(length):
			while stack and temperatures[stack[-1]] < temperatures[i]:
				j = stack.pop()
				result[j] = i - j
			stack.append(i)
		return result


if __name__ == "__main__":
	test_set = [
		[73, 74, 75, 71, 69, 72, 76, 73]
	]
	sol = Solution()
	for x in test_set:
		print(sol.dailyTemperatures(x))
