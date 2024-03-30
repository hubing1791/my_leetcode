# https://leetcode-cn.com/problems/gas-station/
# 2021-12-16

from typing import List


class Solution:
	# 可以类似于双指针的思路选一个起点开始往后走，走不动了将起点后移动，并记录数据变化。反复这样，如果可以走通必然会首尾相接，走不通会再次回到起点。
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		length = len(gas)
		start, end = 0, 0
		gas_left = 0
		for i in range(length):
			if i != 0:
				# 相当于起点后移
				gas_left = gas_left - gas[i - 1] + cost[i - 1]
			else:
				gas_left += gas[i]
			# 获取起点
			start = i
			while gas_left >= 0:
				end = (end + 1) % length
				gas_left = gas_left - cost[end - 1]
				if end == start and gas_left >= 0:
					return end
		return -1

	# 经过试写之后，发现起点不必遍历搜索，起点必须满足条件，即起点获得的油必须多于到达下一个点的油。因此不需要试那么多次，把可能的起点都试一下即可
	# 该方法逻辑正确，问题在于遇到特殊的会因为重复计算而超时
	def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
		length = len(gas)
		for i in range(length):
			if gas[i] < cost[i]:
				pass
			else:
				end = start = i
				gas_left = gas[i]
				while gas_left >= 0:
					end = (end + 1) % length
					gas_left -= cost[end - 1]
					if gas_left < 0:
						break
					else:
						if end == start:
							return start
						else:
							gas_left += gas[end]
		return -1

	# 逻辑对了，性能极差
	def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
		length = len(gas)
		# 留下两个标志位，可以减少重复计算,记录上一次的起始位置和结束位置
		last_start = last_end = 0
		for i in range(length):
			if gas[i] < cost[i]:
				pass
			else:
				# 消除两个七点之间的差
				for j in range(last_start, min(i, last_end)):
					gas_left = gas_left + cost[j] - gas[j]
				end = i
				# 这种情况说明新的起点在上一次结束位置之后
				if end >= last_end:
					gas_left = gas[i]
				else:
					end = last_end

				while gas_left >= 0:
					end = (end + 1) % length
					gas_left -= cost[end - 1]
					if gas_left < 0:
						break
					else:
						if end == i:
							return i
						else:
							gas_left += gas[end]
				last_end = end
				last_start = i

		return -1

	# 官方的
	def canCompleteCircuitoffical(self, gas: List[int], cost: List[int]) -> int:
		length = len(gas)
		start = 0
		while start < length:
			gas_left = gas[start]
			end = start
			while gas_left >= 0:
				# 这么写循环无法终止
				# end = (end + 1) % length
				end = end + 1
				gas_left -= cost[(end - 1) % length]
				if gas_left < 0:
					start = end
				else:
					# 此处不取模，永远无法相等
					# if end == start:
					if end % length == start:
						return end
					else:
						gas_left += gas[end % length]
		return -1


if __name__ == "__main__":
	sol = Solution()
	test_set = [
		[[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]]
	]
	for gas, cost in test_set:
		print(sol.canCompleteCircuit(gas, cost))
