class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def InitLL(list_node_list):
    def dfs(index: int):
        nonlocal length
        if index < length:
            cur_node = ListNode(list_node_list[index])
            cur_node.next = dfs(index + 1)
            return cur_node
        else:
            return None

    length = len(list_node_list)
    return dfs(0)


def showLL(head: ListNode):
    result = []
    cur_node = head
    while cur_node:
        result.append(cur_node.val)
    print(result)
