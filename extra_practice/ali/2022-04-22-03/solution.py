from typing import List


# 两个相相邻修改和不相邻修改
# 比如说a,b,c
def gra(g_list: List[int]):
    # 扫描一遍，得到不相邻修改可以得到的最大变化，然后组合起来，和相邻修改对比。选择可以
    num_r = 0  # 一遍扫描得到原本的值
    chang_not = [[0, i] for i in range(len(g_list))]
    chang_neighbor = [0] * len(g_list)
