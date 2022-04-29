### 98.验证二叉搜索树

[题目链接](https://leetcode-cn.com/problems/validate-binary-search-tree/)

（1）直接中序遍历，使用迭代，在遍历的过程中就进行检验

（2）犯了个低级错误，while里的条件应该是stack or node，整半天没注意到，一直在疑惑

（2）二叉搜索树不允许有相同的值，一开始漏考虑了这个条件



