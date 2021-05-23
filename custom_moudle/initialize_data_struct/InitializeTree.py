class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def InitializeTree(tree_list):
    if not tree_list or not tree_list[0]:
        return None
    length = len(tree_list)

    def dfs(index: int):
        nonlocal length
        if index < length and tree_list[index]:
            node = TreeNode(tree_list[index])
            node.left = dfs(index * 2 + 1)
            node.right = dfs(index * 2 + 2)
        else:
            node = None
        return node

    head = dfs(0)
    return head


if __name__ == "__main__":
    test_set = [5, 1, 4, None, None, 3, 6]
    root = InitializeTree(test_set)
