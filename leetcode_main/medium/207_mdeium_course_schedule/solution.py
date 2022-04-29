# https://leetcode-cn.com/problems/course-schedule/
from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    # 知道是图问题，但是不会写，上题解.大体思路对了，看了题解再写的
    # https://leetcode-cn.com/problems/course-schedule/solution/ke-cheng-biao-by-leetcode-solution/
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
        valid = True

        flag_Courses = [0] * numCourses

        def dfs(v: int):
            nonlocal valid
            if valid:
                if flag_Courses[v] == 0:
                    flag_Courses[v] = 1
                    for u in edges[v]:
                        dfs(u)
                elif flag_Courses[v] == 1:
                    valid = False
                    return
                else:
                    return
                flag_Courses[v] = 2
            else:
                return

        for i in range(numCourses):
            if flag_Courses[i] == 0:
                dfs(i)
        return valid

    # 把能学的课学掉，之后继续学掉新的可以学的课，最后无课剩余就无环
    def canFinish_BFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        dimension_Courses = [0] * numCourses
        visited = 0
        for edge in prerequisites:
            # 此处字典表示，学了某个课之后，可以学对应的列表里的课
            edges[edge[1]].append(edge[0])
            dimension_Courses[edge[0]] += 1

        q = deque([u for u in range(numCourses) if dimension_Courses[u] == 0])
        while q:
            v = q.popleft()
            visited += 1
            for u in edges[v]:
                dimension_Courses[u] -= 1
                if dimension_Courses[u] == 0:
                    q.append(u)
        return visited == numCourses


if __name__ == "__main__":
    sol = Solution()
    sol.canFinish(2, [[1, 0], [0, 1]])
