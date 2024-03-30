class Solution:
	def merge(self, nums1, m, nums2, n):
		nums1_round, nums2_round, write_index = -n - 1, -1, -1  # nums1后面有n个空位
		while nums1_round >= -m - n and nums2_round >= -n:
			if nums1[nums1_round] > nums2[nums2_round]:
				nums1[write_index] = nums1[nums1_round]
				write_index -= 1
				nums1_round -= 1
			elif nums1[nums1_round] < nums2[nums2_round]:
				nums1[write_index] = nums2[nums2_round]
				write_index -= 1
				nums2_round -= 1
			else:
				nums1[write_index], nums1[write_index - 1] = nums2[nums2_round], nums2[nums2_round]
				write_index -= 2  # 这儿一开始写成了-1，就会少退一位
				nums1_round -= 1
				nums2_round -= 1
		if nums1_round == -m - n - 1:
			# 如果是nums2先耗完，因为是有序数组，不需要在处理，只有当nums1先耗完才需要处理
			while nums2_round >= -n:
				nums1[write_index] = nums2[nums2_round]
				write_index -= 1
				nums2_round -= 1
		return nums1

	def merge_smart(self, nums1, m, nums2, n):
		# 利用python自带的函数来解决问题
		# 值是对的，但是python的机制使得nums1已经不是原来的nums1了
		nums1 = nums1[0:m] + nums2
		nums1.sort()
		return nums1

	def merge_smart(self, nums1, m, nums2, n):
		nums1[m:] = nums2  # 修正版
		nums1.sort()


if __name__ == '__main__':
	sol = Solution()
	#	print(sol.merge([0, 0, 3, 0, 0, 0, 0, 0, 0], 3, [-1, 1, 1, 1, 2, 3], 6))
	# print(sol.merge_smart([0, 0, 3, 0, 0, 0, 0, 0, 0], 3, [-1, 1, 1, 1, 2, 3], 6))
	print(sol.merge_smart([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
