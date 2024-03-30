# 踏实的按照字符串处理
class Solution:
	def addBinary(self, a: str, b: str) -> str:
		if len(a) > len(b):
			a, b = b, a
		i = 0
		temp = 0  # 进位
		result = ''
		while i > - len(a):
			i -= 1
			result_temp = temp + int(b[i]) + int(a[i])  # 当前指向位数的计算结果
			if result_temp == 3:
				temp = 1
				result = '1' + result
			elif result_temp == 2:
				temp = 1
				result = '0' + result
			elif result_temp == 1:
				temp = 0
				result = '1' + result
			else:
				temp = 0
				result = '0' + result
		if len(a) == len(b):
			if temp == 1:
				result = '1' + result
				return result
			else:
				return result
		else:
			i = -len(a)
			while i > -len(b):
				i -= 1
				if temp + int(b[i]) == 2:
					temp = 1
					result = '0' + result
				elif temp + int(b[i]) == 1:
					result = b[:i] + '1' + result
					return result
				else:
					result = b[:i] + '0' + result
					return result
		return '1' + result  # 能到达这一步的一定是一直进位，temp=1的情况


if __name__ == '__main__':
	sol = Solution()
	print(sol.addBinary('10', '1'))
	print('ab'[:-2])
