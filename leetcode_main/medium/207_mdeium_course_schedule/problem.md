### 207.课程表

1.先有了简单的思路，按照配对，一顶可以通过先修关系一直向前寻找，可以维护一个set，只要在向前寻找时发现有课已经在set中，那必然出现了循环。思考后，发现这个思路下，必须得按照关系追踪，这在数列中是不方便的。

2.想到了一个改良，生成一个课数目的列表，将对应课位置的值改为它的先修课，之后再验证这种指向是否形成环。但是这种方法没有办法应对a有b，c两个先修课的情况

3.一个笨办法，将关系对按2转化一下，但是相当于是个二级列表指向，然后判断里面有没有循环。但是这样也很麻烦。

4.还是看答案吧，这个涉及了图算法属于知识盲区了。仔细看了下代码，其实就是我3的思路[题解](https://leetcode-cn.com/problems/course-schedule/solution/ke-cheng-biao-by-leetcode-solution/)

5.题解还有广度优先，思路是把能学的课学掉，之后继续学掉新的可以学的课，最后无课剩余就无环


