class Solution:
	@staticmethod
	def ReturnNext(str_num):
		len_str = len(str_num)
		count_ = 0  # 记录重复数字个数
		temp_num = str_num[0]
		result = ''
		for i in range(len_str):
			if i == len_str - 1:
				if str_num[i] == temp_num:
					count_ += 1
					result = result + str(count_) + str(temp_num)
				else:
					result = result + str(count_) + str(temp_num)
					result = result + '1' + str_num[i]
			elif str_num[i] == temp_num:
				count_ += 1
			elif str_num[i] != temp_num:
				result = result + str(count_) + str(temp_num)
				temp_num = str_num[i]
				count_ = 1

		return result

	def countAndSay(self, n: int) -> str:
		result = '1'
		for i in range(n - 1):
			result = self.ReturnNext(result)
		return result


if __name__ == '__main__':
	sol = Solution()
	print(sol.countAndSay(1))
	print(sol.countAndSay(2))
	print(sol.countAndSay(3))
	print(sol.countAndSay(4))
