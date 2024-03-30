# 直接利用函数特性，击败81%，性能还不错
# 官方解答很有意思
class Solution:
	def findMedianSortedArrays(self, nums1, nums2) -> float:
		nums_together = nums1 + nums2
		nums_together.sort()
		len_together = len(nums_together)
		if len_together % 2 == 0:
			result = (nums_together[len_together // 2] + nums_together[len_together // 2 + 1]) / 2
		else:
			result = nums_together[len_together // 2]
		return result

	def findMedianSortedArraysOffical1(self, nums1, nums2) -> float:  # 写一下官方解答1,复杂度log(m+n)
		len_together = len(nums2) + len(nums1)
		result_index = len_together // 2  # 要找的数组下标值的上界

		def getele(k):
			index1, index2 = 0, 0
			while True:
				if index1 == len(nums1):
					return nums2[index2 + k - 1]
				if index2 == len(nums2):
					return nums1[index1 + k - 1]
				if k == 1:
					return min(nums1[index1], nums2[index2])
				newindex1 = min(index1 + k // 2 - 1, len(nums1) - 1)  # 这儿如果不减一可能会越界
				newindex2 = min(index2 + k // 2 - 1, len(nums2) - 1)
				if nums1[newindex1] >= nums2[newindex2]:
					k -= newindex2 - index2 + 1
					# 这里不能直接用k -= k//2 +1 ，因为上一步的min(...)可能会导致减少的范围并不是k//2
					# 而是len(num)和index的差值
					index2 = newindex2 + 1
					# 加一因为index其实指的是第几个，还是因为下标起始的问题
				else:
					k -= newindex1 - index1 + 1
					index1 = newindex1 + 1

		if len_together % 2:
			return getele(result_index + 1)
		else:
			return (getele(result_index) + getele(result_index + 1)) / 2

	def findMedianSortedArraysOffical2(self, nums1, nums2) -> float:  # 写一下官方解答2,复杂度log(min(m+n))
		# 现官方示例解法有问题，对于左右两部分划分存在极端值的情况无法处理
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1
		m, n = len(nums1), len(nums2)
		left_index, right_index = 0, m
		max_left, min_right = 0, 0
		while right_index >= left_index:
			i = (left_index + right_index) // 2
			j = (m + n + 1) // 2 - i


	def findMedianSortedArraysoffice(self, nums1, nums2) -> float: #官方解法，有误
		if len(nums1) > len(nums2):
			return self.findMedianSortedArrays(nums2, nums1)

		infinty = 2 ** 40
		m, n = len(nums1), len(nums2)
		left, right = 0, m
		# median1：前一部分的最大值
		# median2：后一部分的最小值
		median1, median2 = 0, 0

		while left <= right:
			# 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
			# // 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
			i = (left + right) // 2
			j = (m + n + 1) // 2 - i

			# nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
			nums_im1 = (-infinty if i == 0 else nums1[i - 1])
			nums_i = (infinty if i == m else nums1[i])
			nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
			nums_j = (infinty if j == n else nums2[j])

			if nums_im1 <= nums_j:
				median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
				left = i + 1
			else:
				right = i - 1

		return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1


if __name__ == '__main__':
	sol = Solution()
	# sol.findMedianSortedArraysOffical([1, 3], [2, 7])
	print(sol.findMedianSortedArraysoffice([0, 2], [-2 ** 43, -2 ** 42, -2 ** 41, 10]))
	print(-2**39)
