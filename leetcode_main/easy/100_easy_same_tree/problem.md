### 100.判断二叉树是否相同
[判断二叉树是否相同](https://leetcode-cn.com/problems/same-tree)
（1）一开始写了前后续遍历，但是前后序都相同无法确定一个二叉树
（2）仅用循环结果无法判断[1,1]和[1,null,1]的区别
（3）后来在遇到空节点时也写入结果，此时只需要一种遍历即可
（4）直接使用递归判断更快
