class Solution:
	def letterCombinations(self, digits: str):
		if not digits:
			return []
		phone_number = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
						['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]  # 用二级数列来生成呗
		n = len(digits)
		result = ['']
		for i in range(n):
			result_temp = []
			for j in phone_number[int(digits[i]) - 2]:
				for k in result:
					result_temp.append(k + j)
			result = result_temp
		return result


if __name__ == '__main__':
	pass
	# print(len(['']))
	# result = []
	# result_temp = []
	# for i in range(1, 27):
	#	 if i % 3 == 1:
	#		 result_temp = []
	#	 result_temp.append(chr(96 + i))
	#	 if i % 3 == 0:
	#		 result.append(result_temp)
	# print(result)
