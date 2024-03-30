# 这个解法很烂，因为速度实在太慢了，字符串操作过多
# 一开始没有意识到str.replace并没改变str，没写成str=str.replace的形式，造成了死循环

class Solution:
	def romanToInt(self, s: str) -> int:
		dict_rtc = {'IV': 4, 'IX': 9, 'I': 1, 'V': 5,
					'XL': 40, 'XC': 90, 'X': 10, 'L': 50,
					'CD': 400, 'CM': 900, 'C': 100, 'D': 500, 'M': 1000}
		# 上面的字典顺序是又要求的，必须先匹配IV再匹配V
		temp_str, result = s, 0
		roman_chars = list(dict_rtc.keys())
		while len(temp_str):
			for roman_char in roman_chars:
				if temp_str.endswith(roman_char):
					result += dict_rtc[roman_char]
					temp_str = temp_str.replace(roman_char, '', 1)
					break
		return result


if __name__ == '__main__':
	rtint = Solution()
	print(rtint.romanToInt("LVIII"))
	print(rtint.romanToInt("MCMXCIV"))

