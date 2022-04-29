### 16.最接近的三数之和

[题目链接](https://leetcode-cn.com/problems/3sum-closest/)

1.暴力解法显然不行。应该还是先排序后计算，记录上一个计算的值，不停逼近

2.题目没有明说，但是需要思考去重的问题。比如一共有3个1，但是只存在一个用了两个1的答案，需要跳过重复的解。这儿的做法和[15题](https://leetcode-cn.com/problems/3sum/)如出一辙