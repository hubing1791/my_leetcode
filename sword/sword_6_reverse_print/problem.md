### 6.z字变换

[题目链接](https://leetcode-cn.com/problems/zigzag-conversion/)

1.一眼看过去是个规律题，变换的位置是有对应的，当numRows为3时第一行的数对应位置是4n，中间是2n+1，下面是4n+2（从0开始计数）。第一行的位置通项公式为(2\*numRows -2)\*n，其它的具体推算就不写了。可以得知，模(2\*numRows -2)的结果互补的数都在同一行。按这个规律可以分队拼接再组合

2.看了下题解，我和最优解思路一样，不过我的代码简洁些