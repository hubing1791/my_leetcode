### 135.candy
[candy](https://leetcode.cn/problems/candy/)

1.也就是糖果相等时可以小于等于，一遍遍历试试，有相等的下一个就置为1，则可以发的最少。分数增加则加一。
2.错误的第一版没有考虑如果糖果不够减少怎么办
3.遍历一遍找到所有比左右都小的位置，这些位置填1,并记录位置的值，形成一个个区间。第二遍从两个低点之间处理，按递增方向加一。
4.3想的还是很搓，最后想着找到方向改变的转折点即可，分割成一个个单调区间，在单调区间上处理。
5.4可以直接循环，找区间-处理-找区间，相当于实际遍历两遍
6.看题解吧  我是fw [题解](https://leetcode.cn/problems/candy/solutions/533150/fen-fa-tang-guo-by-leetcode-solution-f01p/?envType=study-plan-v2&envId=top-interview-150)