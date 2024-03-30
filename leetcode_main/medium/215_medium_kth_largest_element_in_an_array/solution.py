# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
from typing import List


class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		def partition(left: int, right: int) -> int:
			pivot = left
			while left < right:
				while left < right and nums[right] >= nums[pivot]:
					right -= 1
				while left < right and nums[left] <= nums[pivot]:
					left += 1
				nums[left], nums[right] = nums[right], nums[left]
			nums[left], nums[pivot] = nums[pivot], nums[left]
			#把单等号写成双等号了
			return left

		min_k = len(nums) - k  # 转化为小的问题
		l, r = 0, len(nums) - 1
		while 1:
			index = partition(l, r)
			if index == min_k:
				return nums[min_k]
			elif index < min_k:
				l = index + 1
			else:
				r = index - 1


if __name__ == '__main__':
	test_set = [[[3, 2, 1, 5, 6, 4], 2, 5]
				]
	sol = Solution()
	for x, y, z in test_set[0:]:
		print(str(sol.findKthLargest(x, y)) + '\t' + str(z) + '\n')
