### 116.填充每个节点的下一个右侧节点

[题目链接](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)

1.上来的直接思路，层序遍历然后一直往右连，加个层级标记，同一级继续右连。 

2.可以逐级建立，利用上级留下的next，就可以实现题目要求的进阶