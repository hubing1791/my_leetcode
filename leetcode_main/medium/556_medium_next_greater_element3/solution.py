# https://leetcode-cn.com/problems/next-greater-element-iii/

class Solution:
	# 作废，可行但是麻烦
	def nextGreaterElement_(self, n: int) -> int:
		str_n = str(n)
		length = len(str_n)
		# 用单调栈找出需要用于交换的数
		stack = []
		# max是最靠右的用来换的数的值，在178954中则为8的位置，loc_list则是记录前一个比自己小的数的位置列表
		max_location = 0
		loc_list = [-1] * length
		for i in range(length - 1, -1, -1):
			while stack and str_n[i] > str_n[stack[-1]]:
				pass

	# 修改了思路，找到降序即可
	# 代码里location的a和b和博客记录的相反
	def nextGreaterElement(self, n: int) -> int:
		# 字符串支持随机存取，但是不支持赋值交换
		n_list = []
		n_temp = n
		while n_temp > 0:
			n_list.append(n_temp % 10)
			n_temp //= 10
		n_list.reverse()
		length = len(n_list)
		if length < 2:
			return -1
		location_a = location_b = -1
		# 先找到变为降序的位置
		for i in range(length - 1, 0, -1):
			if n_list[i] > n_list[i - 1]:
				location_a = i-1
				break
		# 找到最靠右的大于左边交换位置数的那个数
		if location_a == -1:
			return -1
		for i in range(location_a + 1, length):
			if n_list[location_a] < n_list[i]:
				location_b = i
		n_list[location_a], n_list[location_b] = n_list[location_b], n_list[location_a]
		n_list[location_a+1:] = list(reversed(n_list[location_a+1:]))
		n_big = 0
		for i in n_list:
			n_big = n_big * 10 + i
		if n_big > 2 ** 31 - 1:
			return -1
		else:
			return n_big

if __name__ == "__main__":
	test_set = [
		1234
	]
	sol = Solution()
	for i in test_set:
		print(sol.nextGreaterElement(i))