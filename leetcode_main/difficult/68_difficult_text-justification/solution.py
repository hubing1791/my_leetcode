# https://leetcode.cn/problems/text-justification/
# 2024-03-30

from typing import List

class Solution:
	def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
		def help(words_need_handle: List[str],min_len_int)-> str:
			leng_handle = len(words_need_handle)
			if leng_handle == 1:
				return words_need_handle[0] + (maxWidth-len(words_need_handle[0]))*" "
			else:
				space_interval,extra_spaces_num = divmod(maxWidth-min_len_int,leng_handle-1)
				space_interval +=1
				res_str = ""
				for x in range(leng_handle-1):
					spaces_num = space_interval + 1 if extra_spaces_num > 0 else space_interval 
					res_str += words_need_handle[x] + spaces_num*" "
					extra_spaces_num -= 1
				res_str += words_need_handle[-1]
				return res_str

		need_handle,min_length,result = [],0,[]
		for word in words:
			add_length = len(word) if min_length == 0 else len(word) +1
			if min_length + add_length > maxWidth:
				result.append(help(need_handle,min_length))
				min_length = len(word)
				need_handle = [word]
			else:
				min_length += add_length
				need_handle.append(word)
		if need_handle:
			txt = " ".join(need_handle)
			result.append(txt + " "*(maxWidth-len(txt)))
		return result
		
