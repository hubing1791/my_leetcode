# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:
    # https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/ceng-xu-bian-li-bfs-rong-yi-li-jie-by-dz-lee/
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        level_order = deque([root])
        result = ''
        while level_order:
            node = level_order.popleft()
            if node:
                result += ('/' + str(node.val))
                level_order.extend([node.left, node.right])
            else:
                result += '/#'
        return result[1:]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        level_order = [TreeNode(int(v)) if v != '#' else None for v in data.split('/')]
        i, j = 0, 1
        while j < len(level_order):
            if level_order[i] is not None:
                level_order[i].left = level_order[j]
                j += 1
                level_order[i].right = level_order[j]
                j += 1
            i += 1
        return level_order[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == '__main__':
    print('dat/abc'.split('/'))
