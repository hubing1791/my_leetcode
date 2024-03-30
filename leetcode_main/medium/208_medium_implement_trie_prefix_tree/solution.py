# https://leetcode-cn.com/problems/implement-trie-prefix-tree/

class Trie:

	def __init__(self):
		self.children = [None] * 26
		self.isEnd = False

	def insert(self, word: str) -> None:
		# 题解这儿相当于用迭代来实现遍历，我一开始习惯性的想到了递归
		node = self
		for char in word:
			index = ord(char) - ord('a')
			if not node.children[index]:
				node.children[index] = Trie()
			node = node.children[index]
		# 最后一个node自然是True
		node.isEnd = True

	def search(self, word: str) -> bool:
		node = self
		for char in word:
			index = ord(char) - ord('a')
			if not node.children[index]:
				return False
			else:
				node = node.children[index]

		return node.isEnd

	def startsWith(self, prefix: str) -> bool:
		node = self
		for char in prefix:
			index = ord(char) - ord('a')
			if not node.children[index]:
				return False
			else:
				node = node.children[index]

		return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
