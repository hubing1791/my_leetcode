# https://leetcode-cn.com/problems/next-permutation/
from typing import List
import itertools


# 想不出，看解答写的
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            exit(0)
        pre_pointer, back_pointer = n - 2, n - 1  # 双指针
        flag = 0  # 标记是否能够找到
        while pre_pointer >= 0:
            if nums[pre_pointer] < nums[back_pointer]:
                flag = 1
                break
            pre_pointer -= 1
            back_pointer -= 1
        if flag == 1:
            back_pointer = n - 1
            while back_pointer:
                if nums[pre_pointer] < nums[back_pointer]:
                    break
                back_pointer -=1
            nums[pre_pointer], nums[back_pointer] = nums[back_pointer], nums[pre_pointer]
            i = 1
            while True:
                if pre_pointer + i < n - i:
                    nums[pre_pointer + i], nums[n - i] = nums[n - i], nums[pre_pointer + i]
                    i += 1
                else:
                    break
        else:
            i = 1
            while True:
                if -1 + i < n - i:
                    nums[-1 + i], nums[n - i] = nums[n - i], nums[-1 + i]
                    i += 1
                else:
                    break
        return nums


if __name__ == '__main__':
    array_1 =[2, 3, 1]
    array = [1, 2, 3, 4, 5]
    sol = Solution()
    print(sol.nextPermutation(array_1))
    # array = [1, 2, 3, 4]
    # arrange_array = list(itertools.permutations(array))
    # arrange_array.sort()
    # for i in arrange_array:
    #     print(i)
