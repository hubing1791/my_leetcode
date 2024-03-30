# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# 2021-12-16

class Solution:
	def reverseParentheses(self, s: str) -> str:
		stack = []
		for i, char_temp in enumerate(s):
			if char_temp == ')':
				s_temp = ''
				char_reverse = stack.pop()
				while char_reverse != '(':
					s_temp += char_reverse
					char_reverse = stack.pop()
				for char_reverse_temp in s_temp:
					stack.append(char_reverse_temp)
				# if stack:
				#	 for char_reverse_temp in s_temp:
				#		 stack.append(char_reverse_temp)
				# else:
				# 可能是（xxx）xxx这种，这样的写法解决不了（xxx）xxx（xx）这种
				# return s_temp + s[i+1:]
			else:
				stack.append(char_temp)
		return ''.join(stack)

	def reverseParenthesesofficial2(self, s: str) -> str:
		# 找到对应的括号并生成对称的字典。
		length = len(s)
		location_dict = dict()
		# # 这是错误版本，没办法应对"ta()usw((((a))))"这样的测试用例。找括号对称可以用栈
		# left, right = 0, length - 1
		# while left < right:
		#	 while left < right and s[left] != '(':
		#		 left += 1
		#	 while left < right and s[right] != ')':
		#		 right -= 1
		#	 if left < right:
		#		 location_dict[left] = right
		#		 location_dict[right] = left
		#		 # 需要从当前位置移开
		#		 right -= 1
		#		 left += 1
		stack = []
		for i in range(length):
			if s[i] == '(':
				stack.append(i)
			if s[i] == ')':
				j = stack.pop()
				location_dict[i] = j
				location_dict[j] = i
		# 用flag标识移动方向
		flag = 1
		i = 0
		result = ''
		tuple_par = {'(', ')'}
		while i < length:
			if s[i] not in tuple_par:
				result += s[i]
				i += flag
			else:
				flag = -flag
				i = location_dict[i] + flag
		return result


if __name__ == "__main__":
	sol = Solution()
	test_set = ["(abcd)",
				"(u(love)i)",
				"(ed(et(oc))el)",
				"a(bcdefghijkl(mno)p)q",
				"ta()usw((((a))))"
				]
	for test_example in test_set:
		print(sol.reverseParentheses(test_example))
