class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		temp = nums.copy()
		temp.sort()  # 默认升序
		i = 0
		j = len(temp) - 1
		while j > i:
			if temp[i] + temp[j] > target:
				j = j - 1
			elif temp[i] + temp[j] < target:
				i = i + 1
			elif temp[i] + temp[j] == target:
				break
		p = nums.index(temp[i])
		nums.pop(p)
		q = nums.index(temp[j])
		if q >= p:
			q = q + 1
		return [p, q]

