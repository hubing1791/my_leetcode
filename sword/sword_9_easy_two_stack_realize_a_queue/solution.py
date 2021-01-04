# https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        else:
            if not self.stack_in:
                return -1
            else:
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
                return self.stack_out.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
