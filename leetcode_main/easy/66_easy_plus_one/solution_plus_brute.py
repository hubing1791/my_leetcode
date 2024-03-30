# 硬按照数组来解决
class Solution:
	def plusOne(self, digits):
		if digits[-1] != 9:
			digits[-1] += 1
			return digits
		else:
			index = -len(digits)
			i = -1
			digits[i] = 0
			while i > index:
				if digits[i - 1] != 9:
					digits[i - 1] += 1
					return digits
				else:
					digits[i - 1] = 0
					i -= 1
		if digits[0] == 0:
			digits.insert(0, 1)
		return digits


if __name__ == '__main__':
	sol = Solution()
	print(sol.plusOne([9, 9, 9, 9, 9]))
