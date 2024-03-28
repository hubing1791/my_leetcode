### 438.find-all-anagrams-in-a-string
[find-all-anagrams-in-a-string](https://leetcode.cn/problems/find-all-anagrams-in-a-string)


1.初始想的是两个set，显然不对，处理不了重复字符
2.滑动窗口加字典，写出来了，但是显然代码很挫。有一个优化点，字母只有26个，根本没必要用字典。构造两个列表比较是否相等即可。