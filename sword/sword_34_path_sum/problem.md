### sword-34-二叉树中和为某一值的路径

[题目链接](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

1.在本题上吃了大亏

- python传列表是引用，第一遍写没注意。而且返回了冗余的数据，设计失误
- 没有仔细读题，想当然觉得树上节点都是正数，想以此剪枝，反而做错了

2.还有BFS的方法：建好一个查父节点的字典parent，然后实际上就是一个层序遍历+额外存储节点对应的当前结果值，每次出队列都进行比较。直到找到根节点，再借助parent查询到路径上所有的数并加入结果