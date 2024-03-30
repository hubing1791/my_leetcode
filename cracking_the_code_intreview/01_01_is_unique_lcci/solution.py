# https://leetcode-cn.com/problems/is-unique-lcci/


class Solution:
	# https://leetcode-cn.com/problems/is-unique-lcci/solution/wei-yun-suan-fang-fa-si-lu-jie-shao-by-zhen-zhu-ha/
	# 上面是参考的题解,定义一个26位的数，用移位运算来解决
	def isUnique(self, astr: str) -> bool:
		mark = 0
		for char in astr:
			move_distance = ord(char) - ord('a')
			if mark & (1 << move_distance):
				return False
			else:
				mark |= 1 << move_distance
		return True
