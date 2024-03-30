# https://leetcode-cn.com/problems/sort-list/solution/

import sys

sys.path.append("..")

from custom_moudle.initialize_data_struct.InitializeListNode import ListNode
from custom_moudle.initialize_data_struct.InitializeListNode import InitLL


class Solution:
	def sortList(self, head: ListNode) -> ListNode:
		# 合并两个排序列表
		def merge(linklist1: ListNode, linklist2: ListNode):
			temp = newhead = ListNode()
			temp1, temp2 = linklist1, linklist2
			while temp1 and temp2:
				if temp1.val <= temp2.val:
					temp.next = temp1
					temp = temp.next
					temp1 = temp1.next
				else:
					temp.next = temp2
					temp2 = temp2.next
					temp = temp.next
			if temp1:
				temp.next = temp1
			if temp2:
				temp.next = temp2
			return newhead.next

		def mergesort(head_merge: ListNode):
			# 对于最后细分成只有一个
			if not head_merge or not head_merge.next:
				return head_merge
			else:
				slow = fast = head_merge
				while fast.next and fast.next.next:
					slow = slow.next
					fast = fast.next.next
				# 断开链表
				mid = slow.next
				slow.next = None
				left = mergesort(head_merge)
				right = mergesort(mid)
				return merge(left, right)

		return mergesort(head)

	# 实现一个不利用递归的版本
	def sortList_1(self, head: ListNode) -> ListNode:
		def merge(linklist1: ListNode, linklist2: ListNode):
			temp = newhead = ListNode()
			temp1, temp2 = linklist1, linklist2
			while temp1 and temp2:
				if temp1.val <= temp2.val:
					temp.next = temp1
					temp = temp.next
					temp1 = temp1.next
				else:
					temp.next = temp2
					temp2 = temp2.next
					temp = temp.next
			if temp1:
				temp.next = temp1
			if temp2:
				temp.next = temp2
			return newhead.next

		# 起个新头节点，方便返回结果
		new_head = ListNode(next=head)
		# 计算链表长度
		cur_node = head
		length = 0
		while cur_node:
			length += 1
			cur_node = cur_node.next
		# 归并排序的主体
		sub_length = 1
		while sub_length < length:
			pre = new_head
			head1 = pre.next
			while head1:
				# 找head2
				cur_node = head1
				for i in range(1, sub_length):
					if cur_node.next:
						cur_node = cur_node.next
					else:
						break
				# 上一步如果节点还够的话，只是找到了head2的前一个节点,接下来找下一轮的head1
				head2 = cur_node.next
				cur_node.next = None
				# 记录下head1的结尾，之后和head2的结尾比较，就可以知道哪个是真的尾巴，然后先切断，之后再连回去
				tail = cur_node
				new_head1 = None
				if head2:
					cur_node = head2
					for i in range(1, sub_length):
						if cur_node.next:
							cur_node = cur_node.next
						else:
							break
					# 下一轮的头，并且先断链接
					new_head1 = cur_node.next
					cur_node.next = None
					# 找到这轮合并的尾巴,在这一开始用的是<,但是遇到链表里有值相同节点会丢失节点
					if tail.val <= cur_node.val:
						tail = cur_node
					# 重新连接链表
				pre.next = merge(head1, head2)
				pre = tail

				head1 = new_head1
			sub_length *= 2
		return new_head.next


if __name__ == "__main__":
	test_set = [4, 2, 1, 3]
	test_set1 = [-470, -346, 602, 625, 819, 861, 439, 722, 706, 800, 894, 855, -385, 597, -101, -84, 558, -16, -236,
				 284, 349, 24, -268, 100, -96, -432, 514, 10, 152, 502, -29, -475, -436, 571, 278, 632, 959, 397, -322,
				 -409, 712, 125, -181, 779, 361, 514, 882, 139, 54, 314, 272, -42, 787, 329, 731, 312, -333, -46, -152,
				 798, -362, 819, 952, 791, 251, -232, 977, -183, -140, -229, -256, -203, -230, 170, -153, -360, 938,
				 -123, -83, 447, 898, 710, -101, 64, 830, -403, 217, -320, 531, -471, 727, -408, -368, 218, 842, 891,
				 -205, -37, -428, -93, 374, 330, -189, -445, 814, 240, 290, 254, -131, -344, 895, 36, -240, 497, 378,
				 67, 927, 115, 193, -256, -497, -82, 406, 637, -417, -452, 518, -205, 600, 26, -373, -489, 476, -287,
				 -100, -361, 783, 101, 147, -233, 703, 613, 931, 572, 21, 498, 379, -168, -350, 166, 139, -62, -285,
				 313, 901, -432, 858, 172, -39, -354, 117, -278, 367, 224, 455, -198, 559, 403, 2, 690, -321, 831, 820,
				 -146, 424, -7, 618, 90, -377, 70, 705, 770, -96, 953, 210, 331, 220, -275, 146, 949, -345, 193, 38,
				 154, 915, -241, -402, -128, -88, 496, -234, 811, 690, 960, -334, 665, -405, -475, 579, -134, 515, -185,
				 395, 304, 318, -246, -386, 541, 191, 59, -138, -161, -317, -207, -134, 202, 925, -140, 416, 57, 665,
				 568, 189, 148, 228, 747, 565, -124, 510, -282, -41, 400, 790, 783, -79, 453, 415, -334, 784, 376, -203,
				 831, -311, 460, 54, 583, 688, 330, 267, 14, -27, 752, -344, -100, -373, 545, 937, 944, 465, -289, 193,
				 735, -170, 403, -153, -482, 41, 335, 301, -350, 845, 634, -213, -486, -406, -10, 71, 986, -107, 418,
				 211, -17, 951, 98, 934, 701, -362, -153, 843, 819, 78, 576, 158, -477, -71, 454, 200, 570, 420, -176,
				 716, 488, -269, 617, 413, 357, 681, 178, 796, 951, 983, 710, 844, 661, 464, -386, 942, -483, -240, 955,
				 -203, 966, 292, 39, -270, 924, 527, 984, 810, -425, -479, 404, 724, -83, 162, 520, -334, -348, 189,
				 949, -99, -443, 136, -475, 216, 415, 80, 530, 127, 635, 831, 794, 778, 335, -101, 577, 853, -118, 976,
				 -354, 537, 9, 575, -430, 685, 51, 707, -26, 584, -482, 968, -194, -91, 832, -84, -330, 188, 171, 712,
				 66, -263, -376, 741, 55, 410, 990, 688, -437, -430, -121, -207, 426, 186, 552, 528, 136, -470, -222,
				 436, 465, 994, -266, -404, 353, 117, 454, -95, 826, 254, 917, 426, -29, 63, -348, 303, 869, -167, 270,
				 -426, 816, 971, -282, 83, 809, 906, 93, -378, 114, 410, -354, 104, -188, 381, 933, 919, 391, -99, 570,
				 274, 717, 11, 637, -185, 914, 918, 277, 397, 561, -262, -451, 752, 55, -68, 134, 401, 257, 591, 489,
				 465, -115, -444, -177, 8, -204, 519, 517, -305, 292, 207, 943, 453, 392, -339, 400, 57, -445, -11, 542,
				 25, -256, 510, 0, 543, -422, 696, 732, 307, 443, -297, 321]
	ll1 = InitLL(test_set1)
	sol = Solution()
	sol.sortList_1(ll1)
