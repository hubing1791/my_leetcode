# https://leetcode-cn.com/problems/multiply-strings/

class Solution:
	# 相当于把每个位数都拆出来了，绝对不会溢出
	def multiply(self, num1: str, num2: str) -> str:
		result_list = [0] * (len(num1) + len(num2))
		for i in range(-1, -len(num1) - 1, -1):
			for j in range(-1, -len(num2) - 1, -1):
				temp_num = int(num1[i]) * int(num2[j])
				if temp_num < 10:
					result_list[i + j + 1] += temp_num
				else:
					result_list[i + j] += 1
					result_list[i + j + 1] += (temp_num - 10)
		for i in range(-1, -len(result_list) - 1, -1):
			while result_list[i] >= 10:
				result_list[i] -= 10
				result_list[i - 1] += 1
		result = ""
		flag = 0
		for i in result_list:
			if i == 0 and flag == 0:
				pass
			else:
				flag = 1
				result = result + str(i)
		return result if result != "" else "0"
