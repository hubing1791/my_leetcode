### sword-11-旋转数组的最小数字

[题目链接](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

1.和搜索旋转数组很像。二分查找的变式。参见题解

2，在left，right的变化上犯了错。因为整除2的原因，right至少要左移一个，所以right=med没问题。 如果left，right只差1，left可能会不移动，因此left每次要加一。把等于单独讨论，等于意味着，最小值在区间内，而且在最右边的更左一点