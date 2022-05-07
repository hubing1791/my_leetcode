### sword-56-2-数组中出现一次的一个数（其它三次）

[题目链接](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/)

1.暴力扫肯定是可以的，用字典扫一遍即可

2.更优方法，将所有数的二进制每位都加起来模3，得到的结果就是只出现一次的。而最终模3和一开始模没区别，在计算过程中就可以做了。这个方法很有意思！！