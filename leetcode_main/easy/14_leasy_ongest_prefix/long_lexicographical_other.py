# 别人的思路，实现了一下，这个想法强大在于，字典顺序比较的例子
# min(abc,bc),bc是大于abc的，因为b顺序大于a
# 还有zip的写法记得学习一下
# 速度没我的快但是优雅
class Solution:
	def longestCommonPrefix(self, strs) -> str:
		if not strs:
			return ''
		str_min, str_max = min(strs), max(strs)
		for i in range(len(str_min)):
			if str_min[i] != str_max[i]:
				return str_min[:i]
		return str_min  # 这种情况对应str——min为空


if __name__ == '__main__':
	solong = Solution()
	print(solong.longestCommonPrefix(["flower", "flow", "flight"]))
	print(solong.longestCommonPrefix(["dog", "racecar", "car"]))
