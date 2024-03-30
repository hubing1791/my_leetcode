# 这个是建立大根堆，最终排序结果为顺序
class HeapSort:
	# 将传入数组整理使得其符合堆
	def __init__(self, heap_list=None) -> None:
		if heap_list is None:
			heap_list = []
		self.heap = heap_list
		self.reform_heap()
		return

	# 需要整体进行处理的情况
	def reform_heap(self, ):
		heap_length = len(self.heap)
		if heap_length <= 1:
			return
		else:
			for i in range((heap_length - 1) // 2, -1, -1):
				self.exchange_element(i, heap_length)

	# 弹出一个元素后的处理
	def exchange_element(self, index: int, length: int):
		if index < length:
			larger, left, right = index, index * 2 + 1, (index + 1) * 2
			if left < length and self.heap[left] > self.heap[index]:
				larger = left
			if right < length and self.heap[right] > self.heap[larger]:
				larger = right
			if larger != index:
				self.heap[index], self.heap[larger] = self.heap[larger], self.heap[index]
				self.exchange_element(larger, length)
		return

	# 添加一个元素
	def push(self, new_num: int):
		self.heap = self.heap + [new_num]
		self.reform_heap()

	# 弹出一个元素
	def pop(self):
		length = len(self.heap) - 1
		if self.heap:
			top = self.heap[0]
			if length <= 1:
				self.heap = self.heap[1:]
				return top
		else:
			return None
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		self.exchange_element(0, length)
		self.heap = self.heap[:-1]
		return top

	# 完整排序
	def sort_all(self):
		length = len(self.heap)
		if self.heap:
			for i in range(length-1,0,-1):
				self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
				self.exchange_element(0,i)
			return self.heap
		else:
			return None


if __name__ == '__main__':
	hs = HeapSort([1, 2, 3, 4, 5, 6, 7])
	print(hs.heap)
	print(hs.pop())
	print(hs.heap)
	hs.push(9)
	hs.sort_all()
	print(hs.heap)
