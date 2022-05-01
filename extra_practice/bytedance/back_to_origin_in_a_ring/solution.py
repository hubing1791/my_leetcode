# https://mp.weixin.qq.com/s/VnGFEWHeD3nh1n9JSDkVUg
# 圆环上有10个点，编号为0~9。从0点出发，每次可以逆时针和顺时针走一步，问走n步回到0点共有多少种走法。

class Solution:
    def BackToOrigin(self, n: int):
        dfs_matrix = [[0] * 10 for i in range(n+1)]
        dfs_matrix[0][0] = 1
        for i in range(1,n):
            for j in range(10):
                dfs_matrix[i][j] = dfs_matrix[i-1][(j-1)%10] + dfs_matrix[i-1][(j+1)%10]
        return
