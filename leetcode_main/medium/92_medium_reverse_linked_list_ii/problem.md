### 92.反转链表2

[题目链接](https://leetcode-cn.com/problems/reverse-linked-list-ii/)

（1）总共需要找到4个节点，left的前节点，left，right的后节点，right，但是存在前后节点不存在的情况。

（2）对于1中的情况，left无前节点添加一个新的头即可使得统一处理方式，而right后节点不存在不影响处理

（3）一开始没看错题了，left和right指位置，当成val值了

（4）第二版写了一个一次遍历版



