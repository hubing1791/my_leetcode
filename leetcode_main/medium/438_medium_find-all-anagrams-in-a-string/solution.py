# https://leetcode.cn/problems/find-all-anagrams-in-a-string
# 2024-03-28

from typing import List,Counter
import copy

class Solution:
	# shitty but right
	def findAnagrams(self, s: str, p: str) -> List[int]:
		char_found_origin,char_need_origin,num_need,result = {},dict(Counter(p)),len(p),[]
		for key in char_need_origin:
			char_found_origin[key] = 0
		char_found,char_need  = copy.deepcopy(char_found_origin),copy.deepcopy(char_need_origin)
		slow_ptr,fast_ptr = 0,0
		while fast_ptr<len(s):
			if s[fast_ptr] in char_need:
				if char_need[s[fast_ptr]]>0:
					char_need[s[fast_ptr]]-=1
					char_found[s[fast_ptr]]+=1
					num_need-=1
				else:
					while slow_ptr<=fast_ptr:
						slow_ptr +=1
						if s[fast_ptr]!=s[slow_ptr-1] and s[slow_ptr-1] in char_need:
							num_need +=1
							char_need[s[slow_ptr-1]]+=1
							char_found[s[slow_ptr-1]]-=1
						if s[fast_ptr]==s[slow_ptr-1]:
							break
			else:
				slow_ptr=fast_ptr+1
				char_found,char_need  = copy.deepcopy(char_found_origin),copy.deepcopy(char_need_origin)
				num_need = len(p)
			fast_ptr +=1
			if num_need == 0:
				result.append(slow_ptr)
				char_found[s[slow_ptr]] -=1
				char_need[s[slow_ptr]]+=1
				num_need+=1
				slow_ptr+=1
		return result
	
	def findAnagrams_offical_1(self, s: str, p: str) -> List[int]:
		s_len, p_len = len(s), len(p)
		
		if s_len < p_len:
			return []

		ans = []
		s_count = [0] * 26
		p_count = [0] * 26
		for i in range(p_len):
			s_count[ord(s[i]) - 97] += 1
			p_count[ord(p[i]) - 97] += 1

		if s_count == p_count:
			ans.append(0)

		for i in range(s_len - p_len):
			s_count[ord(s[i]) - 97] -= 1
			s_count[ord(s[i + p_len]) - 97] += 1
			
			if s_count == p_count:
				ans.append(i + 1)

		return ans

	def findAnagrams_offical_2(self, s: str, p: str) -> List[int]:
		s_len, p_len = len(s), len(p)

		if s_len < p_len:
			return []

		ans = []
		count = [0] * 26
		for i in range(p_len):
			count[ord(s[i]) - 97] += 1
			count[ord(p[i]) - 97] -= 1

		differ = [c != 0 for c in count].count(True)

		if differ == 0:
			ans.append(0)

		for i in range(s_len - p_len):
			if count[ord(s[i]) - 97] == 1:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
				differ -= 1
			elif count[ord(s[i]) - 97] == 0:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
				differ += 1
			count[ord(s[i]) - 97] -= 1

			if count[ord(s[i + p_len]) - 97] == -1:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
				differ -= 1
			elif count[ord(s[i + p_len]) - 97] == 0:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
				differ += 1
			count[ord(s[i + p_len]) - 97] += 1
			
			if differ == 0:
				ans.append(i + 1)

		return ans

if __name__ == "__main__":
	sol = Solution()
	test_cases = [
		["cbaebabacd","abc"],
		["abaacbabc","abc"]
	]
	for s,p in test_cases[1:]:
		print(sol.findAnagrams(s,p))
				

			