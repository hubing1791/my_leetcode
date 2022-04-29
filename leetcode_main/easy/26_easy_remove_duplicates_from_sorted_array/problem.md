### 26.移除有序链表里的重复元素 

[移除有序链表里的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

（1）类似len(xx)这样的，如果写在条件里，每次都会计算从而变慢

（2）这题一开始实现的解法写出了不必要的条件判断语句，写了4个版本。无意间发现for循环慢一些。查资料证实了这一点，但是当迭代对象已经存在时则是for快一点。[参考资料](https://blog.csdn.net/Vector97/article/details/90136777)

