from typing import List


class Solution:
	def QuickSort(self, num_list: List[int]) -> List[int]:
		# 定义快排部分
		def QuickSortHelper(left, right):
			pivot = num_list[left]
			left_temp, right_temp = left, right
			while left_temp < right_temp:
				while left_temp < right_temp and num_list[right_temp] >= pivot:
					right_temp -= 1
				num_list[left_temp] = num_list[right_temp]
				while left_temp < right_temp and num_list[left_temp] <= pivot:
					left_temp += 1
				num_list[right_temp] = num_list[left_temp]
			num_list[left_temp] = pivot
			if left_temp > left + 1:
				QuickSortHelper(left, left_temp - 1)
			if left_temp < right - 1:
				QuickSortHelper(left_temp + 1, right)

		QuickSortHelper(0, len(num_list) - 1)

	def QuickSort_try(self, num_list: List[int]) -> List[int]:
		# 因为后续递归变成了局部变量，这个算法不成立了
		pivot = num_list[0]
		left, right = 0, len(num_list) - 1
		while left < right:
			while left < right and num_list[right] >= pivot:
				right -= 1
			num_list[left] = num_list[right]
			while left < right and num_list[left] <= pivot:
				left += 1
			num_list[right] = num_list[left]
		num_list[left] = pivot
		if left > 1:
			self.QuickSort_try(num_list[:left])
		if left < len(num_list) - 2:
			self.QuickSort_try(num_list[left + 1:])
		print(num_list)
		print(map(id,num_list))


if __name__ == "__main__":
	sol = Solution()
	test_set = [
		[8, 3, 5, 9, 10, 77, 1, 6],
		[6, 3, 5, 1]
	]
	for i in test_set[:1]:
		sol.QuickSort_try(i)
