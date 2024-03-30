# https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
# 2022-05-01

class Solution:
	# n从0开始
	def findNthDigit(self, n: int) -> int:
		if n <= 9:
			return n
		# w位数记录
		num = 1
		# 剩余值
		num_left = n - 9
		while 1:
			# 此时这儿得把位数先加一来判段够不够减，因为n位数个数换算公式的缘故
			num_left -= (num+1) * 9 * 10 ** num
			if num_left > 0:
				num += 1
			else:
				num_left += (num+1)*9 * 10 ** num
				num += 1
				break
		start = 10 ** (num - 1)
		x, y = divmod(num_left, num)
		# y == 0取的是最后一个数，但是下边却最小所以得单独讨论
		if y == 0:
			return (start + x-1) % 10
		else:
			return ((start + x) // 10 ** (num-y)) % 10

if __name__ == '__main__':
	so = Solution()
	re =[]
	tmp =[]
	for x in range(0,200):
		tmp.append(so.findNthDigit(x))
		if x%20 == 19:
			re.append(tmp)
			tmp = []
	print(re)
	print(so.findNthDigit(100))
