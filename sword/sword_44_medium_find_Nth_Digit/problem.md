### sword-44-数字序列中第n位的数

[题目链接](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)

1.很明显是个规律题。n位数的个数，为9*10^(n-1),除了一位数特殊外，此外，n位之前的数的个数是10^（n-1）。由此可以大体算出第n位虽在的区间，再进一步找到数字就可以了

2.需要特别注意在代码的第14，15行的问题，判断剩下还有多少个数的时候，位数和个数的对应关系