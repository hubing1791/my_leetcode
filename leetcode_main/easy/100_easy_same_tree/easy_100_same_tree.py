class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 一开始写了前后续遍历，但是前后序都相同无法确定一个二叉树
# 仅用循环结果无法判断[1,1][1,null,1]的区别
# 如果遇到空节点也写入列表，则只需要一次遍历得到的结果进行比较
class Solution:
    def PreOrderTraverse(self, list_result: list, tree: TreeNode):
        if tree:
            list_result.append(tree.val)
            self.PreOrderTraverse(list_result, tree.left)
            self.PreOrderTraverse(list_result, tree.right)
        else:
            list_result.append(None)  # 为了区分左右子树

    # def InOrderTraverse(self, list_result: list, tree: TreeNode):
    #     if tree:
    #         self.PreOrderTraverse(list_result, tree.left)
    #         list_result.append(tree.val)
    #         self.PreOrderTraverse(list_result, tree.right)
    #     else:
    #         list_result.append(None)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        list_p_pre, list_q_pre = [], []
        self.PreOrderTraverse(list_p_pre, p)
        self.PreOrderTraverse(list_q_pre, q)
        if list_p_pre != list_q_pre:
            return False
        # self.InOrderTraverse(list_p_in, p)
        # self.InOrderTraverse(list_q_in, q)
        # if list_p_in != list_q_in:
        #     return False
        return True

    # 别人的递归解决的思路
    def isSameTreeRecursive(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        # 判断树是否相等,同时层序遍历
        def equal_tree(node1: TreeNode, node2: TreeNode):
            level_order1 = deque([node1])
            level_order2 = deque([node2])
            while level_order1 and level_order2:
                temp_node1 = level_order1.popleft()
                temp_node2 = level_order2.popleft()
                # 值不相等返回
                if temp_node1.val != temp_node2.val:
                    return False
                # 左节点必须同时存在或者不存在
                if temp_node1.left and temp_node2.left:
                    level_order1.append(temp_node1.left)
                    level_order2.append(temp_node2.left)
                elif not temp_node1.left and not temp_node2.left:
                    pass
                else:
                    return False
                # 右节点必须同时存在或者不存在
                if temp_node1.right and temp_node2.right:
                    level_order1.append(temp_node1.right)
                    level_order2.append(temp_node2.right)
                elif not temp_node1.right and not temp_node2.right:
                    pass
                else:
                    return False
            if len(level_order1) != len(level_order2):
                return False
            else:
                return True
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return equal_tree(p,q)
