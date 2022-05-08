# https://leetcode-cn.com/problems/one-away-lcci/
# 2022-05-07

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        length1, length2 = len(first), len(second)
        if length1 < length2:
            first, second = second, first
            length2, length1 = length1, length2
        if length1 - length2 >= 2:
            return False
        if length1 ==1:
            return True
        # 记录差距的数
        count = 0
        # 分别对应两个字符串的指针
        index1, index2 = 0, 0
        while index1 < length1 and index2 < length2:
            if first[index1] == second[index2]:
                index2 += 1
            else:
                if count >= 1:
                    return False
                # 最多长度差一，长度差一只有first指针继续前进，相同都前进
                if length1 == length2:
                    index2 += 1
                count += 1

            index1 += 1
        return True

