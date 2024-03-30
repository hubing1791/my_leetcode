# https://leetcode-cn.com/problems/word-ladder/
# 2022-03-09

import collections
from typing import List


# 这个比较难，直接看的题解
class Solution:
	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		# 首先需要将题目给的数据转化为图。
		# 用于给单词映射到数字
		wordID = dict()
		num_count = 0
		# 记录图
		edge = collections.defaultdict(list)

		# 将一个单词添加进单词到ID的映射
		def add_word(word: str):
			if word not in wordID:
				nonlocal num_count
				wordID[word] = num_count
				num_count += 1

		# 构建图
		def build_graph(word: str):
			add_word(word)
			# 把单词转化为一个字母列表，替换其中一个为*从而构造虚拟节点
			char_list = list(word)
			id1 = wordID[word]
			for i in range(len(char_list)):
				tmp_char = char_list[i]
				char_list[i] = '*'
				new_word = ''.join(char_list)
				add_word(new_word)
				id2 = wordID[new_word]
				edge[id1].append(id2)
				edge[id2].append(id1)
				char_list[i] = tmp_char

		for word in wordList:
			build_graph(word)
		build_graph(beginWord)

		if endWord not in wordID:
			return 0

		# 利用广度优先搜索
		beginID, endID = wordID[beginWord], wordID[endWord]
		graph_queue = collections.deque([])
		# 这是个记录beginID到对应ID距离的数列，因为长度最多为元素个数的两倍，因此用元素个数乘以三就可以了
		dis = [num_count * 3] * num_count
		dis[beginID] = 0
		graph_queue.append(beginID)

		while graph_queue:
			tmp_ID = graph_queue.popleft()
			if tmp_ID == endID:
				return dis[endID] // 2 + 1
			for next_ID in edge[tmp_ID]:
				# 没到达过的才需要更新并加入
				if dis[next_ID] == num_count * 3:
					dis[next_ID] = dis[tmp_ID] + 1
					graph_queue.append(next_ID)

		return 0

	# 双向广度优先
	def ladderLength_bi(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		wordID = dict()
		num_count = 0
		edge = collections.defaultdict(list)

		def add_word(word: str):
			if word not in wordID:
				nonlocal num_count
				wordID[word] = num_count
				num_count += 1

		def build_graph(word: str):
			add_word(word)
			char_list = list(word)
			id1 = wordID[word]
			for i in range(len(char_list)):
				tmp_char = char_list[i]
				char_list[i] = '*'
				new_word = ''.join(char_list)
				add_word(new_word)
				id2 = wordID[new_word]
				edge[id1].append(id2)
				edge[id2].append(id1)
				char_list[i] = tmp_char

		for word in wordList:
			build_graph(word)
		build_graph(beginWord)

		if endWord not in wordID:
			return 0

		beginID, endID = wordID[beginWord], wordID[endWord]
		begin_queue, end_queue = collections.deque([beginID]), collections.deque([endID])
		# 到达起点和终点的距离分别为两个数列
		begin_dis, end_dis = [num_count * 3] * num_count, [num_count * 3] * num_count
		begin_dis[beginID], end_dis[endID] = 0, 0

		while begin_queue or end_queue:
			begin_size = len(begin_queue)
			# 不能写成for _ in begin_queue,因为可能会变化
			for _ in range(begin_size):
				tmp_ID = begin_queue.popleft()
				if end_dis[tmp_ID] != num_count * 3:
					return (end_dis[tmp_ID] + begin_dis[tmp_ID]) // 2 + 1
				for next_ID in edge[tmp_ID]:
					if begin_dis[next_ID] == num_count * 3:
						begin_dis[next_ID] = begin_dis[tmp_ID] + 1
						begin_queue.append(next_ID)

			end_size = len(end_queue)
			for _ in range(end_size):
				tmp_ID = end_queue.popleft()
				if begin_dis[tmp_ID] != num_count * 3:
					return (end_dis[tmp_ID] + begin_dis[tmp_ID]) // 2 + 1
				for next_ID in edge[tmp_ID]:
					if end_dis[next_ID] == num_count * 3:
						end_dis[next_ID] = end_dis[tmp_ID] + 1
						end_queue.append(next_ID)

		return 0


if __name__ == "__main__":
	test_set = [
		["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]]
	]
	sol = Solution()
	for start_word, end_word, word_list in test_set:
		sol.ladderLength(start_word, end_word, word_list)
