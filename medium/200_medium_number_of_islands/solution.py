# https://leetcode-cn.com/problems/number-of-islands/
from typing import List


class Solution:
    # 这是初始思路，写了一半发现巨复杂，放弃
    def numIslands_useless(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        length, width = len(grid[0]), len(grid)

        # 定义一个函数用来搜索一个点坐标在结果坐标集的位置
        def search(coordinate: List, coor_set: List):
            for i in range(len(coor_set)):
                if coordinate in coor_set[i]:
                    return i
            return -1

        # 存岛的结果点集的结果，里面是一个个set，一个set对应于一个在一起的岛屿上的点
        result_list = []
        for i in range(width):
            for j in range(length):
                if grid[i][j]:
                    # 判断一个岛周围的点是否在结果集中
                    flag = 0
                    if i - 1 > -1 and grid[i - 1][j]:
                        pass

    def numIslands(self, grid: List[List[str]]) -> int:
        length, width = len(grid[0]), len(grid)
        result = 0

        # 沉岛
        def land(x, y):
            grid[x][y] = "0"
            if x - 1 >= 0 and grid[x - 1][y] == "1":
                land(x - 1, y)
            if x + 1 < width and grid[x + 1][y] == "1":
                land(x + 1, y)
            if y - 1 >= 0 and grid[x][y - 1] == "1":
                land(x, y - 1)
            if y + 1 < length and grid[x][y + 1] == "1":
                land(x, y + 1)

        for i in range(width):
            for j in range(length):
                if grid[i][j] == "1":
                    result += 1
                    land(i, j)
        return result


if __name__ == "__main__":
    list_1 = [1, 2, 3]
    for i in range(len(list_1)):
        list_1[i] += 1
    print(list_1)
