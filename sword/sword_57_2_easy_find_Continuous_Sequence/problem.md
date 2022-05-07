### sword-57-2-和为s的连续正序列

[题目链接](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)

1.这道题我首先考虑了可能的序列范围，首先，假设为n个，假设里面最小的数为a，那么总和就是 a*n + (n-1)n/2，n从2开始增大，计算这个式子的解，a最小为1，会知道n的范围。

2.n的范围没必要精确计算，当a取1时。n方加n为2倍target，直接开方得范围即可

3.没仔细看题解了，我的方法优于最优解。