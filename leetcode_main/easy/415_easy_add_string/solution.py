# https://leetcode-cn.com/problems/add-strings

class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		if len(num1) < len(num2):
			num1, num2 = num2, num1
		num2 = '0' * (len(num1) - len(num2)) + num2
		carry_bit = 0
		result = ''
		for i in range(-1, -len(num1) - 1, -1):
			int1 = int(num1[i])
			int2 = int(num2[i])
			result = str((int1 + int2 + carry_bit) % 10) + result
			carry_bit = (int1 + int2 + carry_bit) // 10
		if carry_bit:
			return '1'+result
		else:
			return result


if __name__ == '__main__':
	pass
