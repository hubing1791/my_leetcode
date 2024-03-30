# https://leetcode-cn.com/problems/minimum-window-substring/
from collections import defaultdict


class Solution:
	# 想用集合子集判断，无法解决，‘a’,'aa'的问题
	def minWindow(self, s: str, t: str) -> str:
		len_s = len(s)
		set_t = set(t)
		i = 0
		result = []
		while i < len_s:
			flag = 0  # 是否找到的flag
			j = i + 1
			set_sub = set(s[i])
			# 用取出的字符串制作成一个集合
			# 假如t是取出字符串的子集，中找到了一个段
			while j < len_s and not set_t.issubset(set_sub):
				set_sub.add(s[j])
				j += 1
			if j <= len_s and set_t.issubset(set_sub):
				flag = 1
				while 1:
					set_sub.remove(s[i])
					if set_t.issubset(set_sub):
						i += 1
					else:
						break
			if flag:
				result.append(s[i:j])
			i = j
		return min(result, key=len)

	# 用字典实现
	def minWindow2(self, s: str, t: str) -> str:
		# 字典记录t的字母和个数
		dict_t = defaultdict(int)
		# 建立一个t的字典，defaultdict会自动初始化
		for char in t:
			dict_t[char] += 1
		count_num = len(t)
		# 把最小长度设为s长度即可，因为任何一个子字符串长度不会超过它，初始化的min_len就是用来更新的，保证足够大就行
		min_len = len(s) + 1
		length = len(s)
		left = right = 0
		result = ''
		while right < length:
			# 如果s里遍历到了t里的字符，那就把count_num减少
			if dict_t[s[right]] > 0:
				count_num -= 1
			# 每一轮对于t形成的字典都减一，这样当遍历到count_num为零时，代表着
			# 当前遍历到的字符串已经包含了目标字符串，而再移动left，将字典值继续加，当再次破坏了
			# count_num=0的时候，意味着一个子字符串就得到了
			dict_t[s[right]] -= 1
			right += 1
			while count_num == 0:
				# 在这，如果s[left]不是一个在t里的字符，则这儿只可能为负数
				# 如果是不在t中的字母，在字典值恢复为零时已经被滑过去了，不会进入判断影响count_num的值
				if dict_t[s[left]] == 0:
					count_num += 1
				if right - left < min_len:
					result=s[left:right]
					min_len = right - left
				# 一开始下面这个操作忽视了
				dict_t[s[left]] += 1
				left += 1
		return result


if __name__ == '__main__':
	test_set = [
		["ADOBECODEBANC", "ABC"],
		["a", "aa"]
	]
	sol = Solution()
	for x, y in test_set[0:]:
		print(sol.minWindow2(x, y))
