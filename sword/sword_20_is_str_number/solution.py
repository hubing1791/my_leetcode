# https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/
# 2022-04-25
import enum

from enum import Enum


class Solution:
	def isNumber(self, s: str) -> bool:
		# 官方题解实垃，参考了下别人的
		states = [
			{' ': 0, 's': 1, 'd': 2, '.': 4},  # 0. 起始的空格
			{'d': 2, '.': 4},				  # 1. 最初的正负号
			{'d': 2, '.': 3, 'e': 5, ' ': 8},  # 2. 起始整数
			{'d': 3, 'e': 5, ' ': 8},		  # 3. 小数点后的整数
			{'d': 3},						  # 4. 空格直接到.，等待一个整数到4，之所以不可以直接到3，因为单独的.非法
			{'s': 6, 'd': 7},				  # 5. 'e'
			{'d': 7},						  # 6. 指数符号后面的正负号
			{'d': 7, ' ': 8},				  # 7. 指数的数部分
			{' ': 8}						   # 8. 结束空格
		]
		p = 0
		for c in s:
			if '0' <= c <= '9':
				t = 'd'
			elif c in "+-":
				t = 's'
			elif c in "eE":
				t = 'e'
			elif c in ". ":
				t = c
			else:
				t = '?'
			if t not in states[p]: return False
			p = states[p][t]
		return p in (2, 3, 7, 8)
