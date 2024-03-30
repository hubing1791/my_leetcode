# https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-by-leetcode-s/
# 2022-04-25
from typing import List


class Solution:
	def minArray(self, numbers: List[int]) -> int:
		# 取最后一个数作为标记
		right, left = len(numbers) - 1, 0
		while left < right:
			med = (left + right) // 2
			if numbers[med] < numbers[right]:
				# 因为整除2的原因，right至少要左移一个
				right = med
			elif numbers[med] > numbers[right]:
				# 如果left，right只差1，left可能会不移动
				left = med + 1
			else:
				right -= 1
		return numbers[left]


if __name__ == '__main__':
	sol = Solution()
	print(sol.minArray([2, 2, 2, 0, 1]))
