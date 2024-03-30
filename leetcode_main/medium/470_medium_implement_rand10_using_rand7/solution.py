import random


def rand7():
	return random.randint(1, 7)


class Solution:
	def rand10(self):
		randx = 7 * (rand7() - 1) + rand7()
		if randx <= 40:
			return randx % 10 + 1
		else:
			return self.rand10()