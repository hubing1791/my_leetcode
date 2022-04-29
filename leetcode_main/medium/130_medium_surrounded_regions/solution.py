# https://leetcode-cn.com/problems/surrounded-regions/solution/
# 2020-10-29

from typing import List


class Solution:
    # 深度优先搜索
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        # 不可以像下面这样生成
        # location_list = [[0] * n ] * m
        location_list = [[0] * n for i in range(m)]

        def DFS(x, y):
            # 不需要到达边界，在边界上本身就有一次循环
            if board[x][y] == "O":
                location_list[x][y] = 1
                # 一开始把位置参数写成[-1,-1]这样了
                for xm, ym in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    # 之前有第三个条件没加，会导致"O"很多时无限递归
                    if 0 <= x + xm < m and 0 <= y + ym < n and location_list[x + xm][y + ym] == 0:
                        DFS(x + xm, y + ym)

        for i in range(m):
            if board[i][0] == "O":
                DFS(i, 0)
            if board[i][n - 1] == "O":
                DFS(i, n - 1)
        for i in range(1, n):
            if board[0][i] == "O":
                DFS(0, i)
            if board[m - 1][i] == "O":
                DFS(m - 1, i)
        for i in range(m):
            for j in range(n):
                if location_list[i][j] == 0:
                    board[i][j] = "X"

    # 广度优先搜索
    def solve1(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        loc_list = []
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'A'
                loc_list.append([i, 0])
            if board[i][n - 1] == 'O':
                board[i][n - 1] = 'A'
                loc_list.append([i, n - 1])
        if n > 2:
            for i in range(1, n - 1):
                if board[0][i] == 'O':
                    board[0][i] = 'A'
                    loc_list.append([0, i])
                if board[m - 1][i] == 'O':
                    board[m - 1][i] = 'A'
                    loc_list.append([m - 1, i])
        while loc_list:
            x, y = loc_list.pop(0)
            for xm, ym in [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]:
                if 0 < xm < m - 1 and 0 < ym < n - 1 and board[xm][ym] == 'O':
                    board[xm][ym] = 'A'
                    loc_list.append([xm, ym])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'



if __name__ == "__main__":
    sol = Solution()
    test_set = [
        [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    ]
    for test_entity in test_set:
        sol.solve(test_entity)
