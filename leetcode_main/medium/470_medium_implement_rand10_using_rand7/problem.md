### 470,用 Rand7() 实现 Rand10()

[题目链接](https://leetcode-cn.com/problems/implement-rand10-using-rand7/)

（1）经典实现方式，先转化成一个均匀的49上的分布，对于多出来的再调用子集一次即可，连续不中的概率会持续降低

（2）题解给了继续利用被拒绝的数的算法，但是代码反而便繁琐了，效率没有明显提升



