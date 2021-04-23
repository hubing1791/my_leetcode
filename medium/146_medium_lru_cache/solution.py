# https://leetcode-cn.com/problems/lru-cache/


class DlinkedNode:
    def __init__(self, key: int = 0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # 初始化字典作为hashmap
        self.cache = dict()
        # 初始化头尾节点
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        # 容量和当下的占用量
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            # 先断开
            node.prev.next = node.next
            node.next.prev = node.prev
            # 插到头节点后
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node

            return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DlinkedNode(key, value)
            # 加入hash表
            self.cache[key] = node
            # 添加到头节点后
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            # 判断是否溢出,如果溢出删除
            self.size += 1
            if self.size > self.capacity:
                del_key = self.tail.prev.key
                self.cache.pop(del_key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                self.size -= 1
        else:
            self.cache[key].value = value
            node = self.cache[key]
            # 先断开
            node.prev.next = node.next
            node.next.prev = node.prev
            # 插到头节点后
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
