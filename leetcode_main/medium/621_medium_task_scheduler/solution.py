# https://leetcode-cn.com/problems/task-scheduler/
from typing import List
from collections import defaultdict, Counter


class Solution:
	# 先用一个字典把所有任务数出来，再用一个集合把所有任务类型数出来，用一个字典表示任务处理器，
	# 每次一个新任务到达，对应的任务类型的value+n，每一轮对不是零的任务类型-1模拟冷却。尽可能
	# 从数好的任务里取除任务处理器里已经冷却完成的任务
	def leastInterval(self, tasks: List[str], n: int) -> int:
		tasks_all = defaultdict(int)
		tasks_kinds = set()
		# 生成任务和对应个数的字典，以及任务类型的集合
		for i in tasks:
			tasks_all[i] += 1
			tasks_kinds.add(i)
		scheduler = defaultdict(int)

		# 模拟过程
		time_sum = 0
		while tasks_kinds:
			for i in tasks_kinds:
				if scheduler[i] == 0:
					# +n表示需要n的冷却，任务减一后判断如果是0直接把集合里的类型去掉，以后就不用遍历了
					# 应该加n+1，因为处理还需要1个时间单位
					scheduler[i] += n + 1
					tasks_all[i] -= 1
					if tasks_all[i] == 0:
						tasks_kinds.remove(i)
					break
			for i in scheduler.keys():
				if scheduler[i] > 0:
					scheduler[i] -= 1
			time_sum += 1
		return time_sum

	# 第一版方法，因为用的是set，所以在循环取任务时会出问题。要让时间尽可能短，应该总是优先取数量最多的任务
	# 这个对于特别大的数据会超时
	def leastInterval_1(self, tasks: List[str], n: int) -> int:
		tasks_all = defaultdict(int)
		# 生成任务和对应个数的字典，以及任务类型的集合
		for i in tasks:
			tasks_all[i] += 1
		scheduler = defaultdict(int)
		tasks_all = dict(tasks_all)

		# 模拟过程
		time_sum = 0
		while 1:
			temp_list = sorted(tasks_all.keys(), key=lambda item: tasks_all[item], reverse=True)
			if tasks_all[temp_list[0]] == 0:
				return time_sum
			for i in temp_list:
				if scheduler[i] == 0:
					scheduler[i] += n + 1
					tasks_all[i] -= 1
					break
			for i in scheduler.keys():
				if scheduler[i] > 0:
					scheduler[i] -= 1
			time_sum += 1

	# 官方解答
	def leastInterval_2(self, tasks: List[str], n: int) -> int:
		freq = Counter(tasks)

		# 任务总数
		m = len(freq)
		nextValid = [1] * m
		# 直接列表化，因为任务具体的名字A,B啥的此时变得不重要了
		rest = list(freq.values())

		time = 0
		for i in range(len(tasks)):
			time += 1
			# 这个找的是还有剩余次数的任务中的最小的剩余时间
			minNextValid = min(nextValid[j] for j in range(m) if rest[j] > 0)
			# 最小的下次有效时间和总用时中较大的一个就是总时间，
			time = max(time, minNextValid)

			best = -1
			# 理论上来说接下来的部分才是在逻辑感觉上先执行的部分，即先分配后计算时间，下面的内容是分配的部分
			for j in range(m):
				# 寻找到剩余次数最多的那个
				if rest[j] and nextValid[j] <= time:
					if best == -1 or rest[j] > rest[best]:
						best = j

			nextValid[best] = time + n + 1
			rest[best] -= 1

		return time


if __name__ == "__main__":
	sol = Solution()
	# sol.leastInterval_1(["A", "A", "A", "B", "B", "B"], 2)
	sol.leastInterval_2(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
