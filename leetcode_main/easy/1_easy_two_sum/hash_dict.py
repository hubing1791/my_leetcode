class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		hash_dict = {}
		for i in range(len(nums)):
			if hash_dict.get(target - nums[i]) is not None:
				return [i, hash_dict.get(target - nums[i])]
			hash_dict[nums[i]] = i  # 找不到就加入字典，相当于无法匹配的扔进字典，让后面取出的数去尝试匹配

