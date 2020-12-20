# 官方解答基于动态规划的代码实现
class Solution:
    def maxSubArray(self, nums):
        loop_index = len(nums)
        for i in range(1, loop_index):
            if nums[i - 1] + nums[i] > nums[i]:
                nums[i] = nums[i - 1] + nums[i]
        return max(nums)

    # https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/
    @staticmethod
    def PushUp(nums_1, nums_2):
        # result数列四个值分别为区间左边最大子段和，区间右边最大子段和，区间内最大子段和，区间和
        result = [0, 0, 0, 0]
        result[0] = max(nums_1[3] + nums_2[0], nums_1[0])
        result[1] = max(nums_2[3] + nums_1[1], nums_2[1])
        result[2] = max(nums_1[2], nums_2[2], nums_2[0] + nums_1[1])
        result[3] = nums_2[3] + nums_1[3]
        return result

    def get_push(self, nums, left, right):
        if right == left:
            return [nums[left], nums[left], nums[left], nums[left]]
            # 这一步之前下标写错了，写成了0，结果固定输出nums[0]
        med_num = (left + right) >> 1
        result_1 = self.get_push(nums, left, med_num)
        result_2 = self.get_push(nums, med_num + 1, right)
        return self.PushUp(result_1, result_2)

    def maxSubArrayDivideAndConquer(self, nums):
        return max(self.get_push(nums, 0, len(nums) - 1))


if __name__ == '__main__':
    sol = Solution()
    # print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(sol.maxSubArrayDivideAndConquer([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
