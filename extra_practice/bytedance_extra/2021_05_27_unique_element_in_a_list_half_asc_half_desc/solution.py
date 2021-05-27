# 数组先递增后递减，求数组内不重复的数
from typing import List


class Solution:
    def UniqueElement(self, num_list: List):
        result = 0
        length = len(num_list)
        left, right = 0, length - 1
        # 看数组情况，如果最高点可以有一段平的，那最后right会在left左边，且差值为2
        while left <= right:
            if num_list[left] == num_list[right]:
                temp = num_list[left]
                while num_list[left] == temp:
                    left += 1
                while num_list[right] == temp:
                    right -= 1
            elif num_list[left] > num_list[right]:
                result += 1
                right -= 1
            else:
                result += 1
                left += 1
        if left - right == 2:
            result += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    test_set = [
        [1, 2, 3, 4, 7, 5, 4]
    ]
    for i in test_set:
        print(sol.UniqueElement(i))
