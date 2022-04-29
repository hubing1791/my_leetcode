### 44.通配符匹配

[题目链接](https://leetcode-cn.com/problems/wildcard-matching/)

1.对于匹配字串扫描，遇到a-z直接同步前进匹配，遇到*应该是可以不停进直到匹配到。但是*存在一些需要细致考虑的地方。例如“\*b”可以匹配“abbb”，在扫描到第一个b不需要停止。而“\*b?b”也可以匹配，但是要及时停止。何处停止就是个问题。这儿考虑可以利用回溯，亦或者直接分支并及时剪枝（写一个递归的算法），只要有一个匹配成功就继续。

2.直接看了题解了，1里说的方法肯定可行但是即便写出来估计也效率太差。参考下答案的动态规划和贪心做。