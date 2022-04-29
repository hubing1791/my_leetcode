### 15.三数之和

[三数之和](https://leetcode-cn.com/problems/3sum)
（1）某次循环中删除了列表元素，后续循环会受影响
（2）[一个很好的解释](https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/)这个方法巧妙在，排序后判断，当nums[i]>0时可以直接返回了，因为后面不再有结果了
（3）题目使用了排序来减少循环的复杂度，我写的通俗方法复杂度太高（虽然已经通过下标递增减少了复杂度）

