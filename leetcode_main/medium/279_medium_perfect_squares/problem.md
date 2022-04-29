### 279.完全平方数

[题目链接](https://leetcode-cn.com/problems/perfect-squares/)

1.一个关键问题既是如何减少尝试次数，上来就想到的是，从大的开始试。然后在函数内部写一个递归，同时要维护一个最多尝试次数用于及时剪枝。最后实现效果还是比较好的

2.看了题解，数学法不说了，还有动态规划法。动态规划法值得学一下[动态规划的官方题解](https://leetcode-cn.com/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode-solut-t99c/)

3.动态规划法效率远差于暴力加剪枝，实际上，剪枝法避免了大量不必要的尝试，而动态规划法还是遍历了所有的情况



