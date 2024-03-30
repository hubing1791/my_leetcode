class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0:
			return False
		temp_num = x
		regx = 0
		flag = len(str(x)) % 2  # 判断这个数是否是奇数位数，奇数位数时处理略有不同
		round_num = len(str(x)) // 2
		while round_num > 0:
			regx = regx * 10 + (temp_num % 10)  # 将x的后半部分逆序输出为regx
			temp_num //= 10  # 去掉最后一位
			round_num -= 1
		if flag:
			temp_num //= 10
		return temp_num == regx


if __name__ == '__main__':
	sol = Solution()
	sol.isPalindrome(123467321)
