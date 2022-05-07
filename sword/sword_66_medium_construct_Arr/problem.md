### sword-66-构建乘积数组

[题目链接](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)

1.因为不能使用除法的要求，不能使用先计算乘积再除以对应的数的办法了。

2.看了题解，从头遍历，相乘一次。再回头遍历，相乘一次，只要合理错开即可。见代码