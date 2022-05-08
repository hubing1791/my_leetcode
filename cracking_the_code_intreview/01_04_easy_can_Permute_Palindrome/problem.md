### cracking-01-04-回文排列

[题目链接](https://leetcode-cn.com/problems/palindrome-permutation-lcci/)

1.是某个回文串的条件是，统计全部字符，最多有一个奇数出现，其它都是偶数个

2.看到了评论区提出的新奇解法，即用二进制位表示是否出现。

3.result & (result - 1) == 0的结果可以表示result里1的个数是否只有一个，只有一个因为借位的关系，1会错开。2个及以上用不完，就不等于0了