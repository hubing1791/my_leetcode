### sword-53-二叉搜索树的第k大节点

[题目链接](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)

1.利用二叉树的中序遍历，然后建立一个大小为k的数组，遍历时，没装满时添加，装满后一边加一边删。最后数组的第一个就是需要的结果