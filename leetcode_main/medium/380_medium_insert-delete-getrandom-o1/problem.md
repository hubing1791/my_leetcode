### 380.insert-delete-getrandom-o1
[insert-delete-getrandom-o1](https://leetcode.cn/problems/insert-delete-getrandom-o1)

1.看了题目要求，意识到这应该是个伪集合，使得该集合存在类似下标的索引，然后通过随机数访问。完全没思路，抄题解。
2.看了题解感觉完全是投机取巧啊，利用了python内置的操作。我不接受，理论上字典加双向链表才是真理吧。
3.收回，2的结论是我没有仔细看代码，将需要删除的量换到最后一位然后删除就可以实现o（1）