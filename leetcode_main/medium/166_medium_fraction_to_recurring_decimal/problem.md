### 166.分数到小数

[题目链接](https://leetcode-cn.com/problems/fraction-to-recurring-decimal/)

1.查了下判断除尽的条件，一个思路：先判断是否是循环小数，如果是，则进行循环到重复一次，就可以得到循环节了。这个思路就需要 1）判断：是否可以除尽 2）寻找循环节

2.看了题解，我想多了，整数部分使用长除法解决，小数部分找循环节是核心。[题解链接](https://leetcode-cn.com/problems/fraction-to-recurring-decimal/solution/fen-shu-dao-xiao-shu-by-leetcode-solutio-tqdw/)

3.写的第一版本有问题，并不是所有小数部分都是循环节，我直接看是否循环，然后将所有的小数部分弄成了循环节。

