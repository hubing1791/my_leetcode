class Solution:
	def removeDuplicates(self, nums):
		if not nums:
			return 0
		i = 0
		temp_num = nums[0]
		while i < len(nums) - 1:
			if temp_num == nums[i] and temp_num == nums[i + 1]:
				nums.pop(i)
			else:
				i += 1
				temp_num = nums[i]
		return i + 1

	def removeDuplicatesDiff(self, nums):  # 写一个不使用pop的
		if not nums:
			return 0
		i, j = 0, 0
		while j < len(nums) - 1:
			if nums[j] == nums[i] and nums[j + 1] == nums[i]:
				j += 1
			else:
				i += 1
				j += 1
				nums[i] = nums[j]
		return i + 1

	# 这儿可以继续优化的点，反正无论如何都要判断j+1，不如值判断j+1，并且每次都要j+=1
	def removeDuplicatesDiffOpt(self, nums):
		if not nums:
			return 0
		i, j = 0, 0
		k = len(nums) - 1
		while j < k:
			j += 1
			if nums[j] != nums[i]:
				i += 1
				nums[i] = nums[j]
		return i + 1

	def removeDuplicatesDiffOptFor(self, nums):  # 用for循环实现会不会更快,结果更慢了
		if not nums:
			return 0
		i = 0
		k = len(nums)
		for j in range(k):
			if nums[j] != nums[i]:
				i += 1
				nums[i] = nums[j]
		return i + 1


if __name__ == '__main__':
	sol = Solution()
	print(sol.removeDuplicatesDiffOptFor([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
