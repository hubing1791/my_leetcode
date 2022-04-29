---
title: 2021年第三季度刷题整理
author: not_you
date: 2021-06-30 00:00:00 +0800
categories: ["leetcode"]
tags: [刷题]

---

6月一整个月忙东忙西没咋写代码，手又有点生了==

碎碎念一下，还是得保持自律啊TvT

### git链接

[我的leetcode刷题记录](https://github.com/hubing1791/my_leetcode)

### 279.完全平方数

[题目链接](https://leetcode-cn.com/problems/perfect-squares/)

1.一个关键问题既是如何减少尝试次数，上来就想到的是，从大的开始试。然后在函数内部写一个递归，同时要维护一个最多尝试次数用于及时剪枝。最后实现效果还是比较好的

2.看了题解，数学法不说了，还有动态规划法。动态规划法值得学一下[动态规划的官方题解](https://leetcode-cn.com/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode-solut-t99c/)

3.动态规划法效率远差于暴力加剪枝，实际上，剪枝法避免了大量不必要的尝试，而动态规划法还是遍历了所有的情况



### 136.只出现一次的数字

[题目链接](https://leetcode-cn.com/problems/single-number/)

1.题目要求线性复杂度，最好不使用额外空间。线性复杂度不难，可上集合，如何不使用额外空间思路有点卡住了。

2.看了下题解豁然开朗，全部异或一下解决



### 142.环形链表2

[题目链接](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

1.不进阶很好实现，见git。借助集合即可

2.空间复杂度o(1)需要借助快慢指针，思考过程复杂一些。[官方题解](https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/)



### 待续



