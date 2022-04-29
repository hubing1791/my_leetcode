### 1190.反转每对括号间的子串

[题目链接](https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/)

1.一眼看去用栈加一个队列来实现即可。写的时候实际想了一下，也用不上队列，可以在队列的部分直接用字符串连接然后再取值放回去。

2，答案的思路二值得一看，参考实现了下。思路是从两头开始遍历，碰到括号改变方向。