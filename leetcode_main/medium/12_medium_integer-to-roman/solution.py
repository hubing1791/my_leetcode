# https://leetcode.cn/problems/integer-to-roman/
# 2024-03-30

class Solution:
	def intToRoman(self, num: int) -> str:
		sp_mod = [
			(1000,"M",True),
			(900,"CM",False),
			(500,"D",True),
			(400,"CD",False),
			(100,"C",True),
			(90,"XC",False),
			(50,"L",True),
			(40,"XL",False),
			(10,"X",True),
			(9,"IX",False),
			(5,"V",True),
			(4,"IV",False),
			(1,"I",True),
		]
		result = ""
		for nn,char,should_divide in sp_mod:
			if should_divide:
				char_num,num = divmod(num,nn)
				result += char_num * char
			else:
				if num>= nn:
					num -=nn
					result+=char
			if num == 0:
				break
		return result
	
	# actually slower
	def intToRoman_opt(self, num: int) -> str:
		sp_mod = [
			(1000,"M"),
			(900,"CM"),
			(500,"D"),
			(400,"CD"),
			(100,"C"),
			(90,"XC"),
			(50,"L"),
			(40,"XL"),
			(10,"X"),
			(9,"IX"),
			(5,"V"),
			(4,"IV"),
			(1,"I"),
		]
		result = ""
		for nn,char in sp_mod:
			while num>= nn:
				num -=nn
				result+=char
			if num == 0:
				break
		return result