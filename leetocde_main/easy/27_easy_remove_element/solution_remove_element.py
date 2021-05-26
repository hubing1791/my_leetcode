# 双指针一前一后汇聚（其实就是下标即可解决）
class Solution:
    def removeElement(self, nums, val):
        cycle_round = len(nums)
        if cycle_round == 0:
            return 0
        i, j = 0, cycle_round - 1
        while 1:
            if nums[i] != val:
                i += 1
            if nums[j] == val:
                j -= 1
            if i > j:
                break
            if nums[i] == val and nums[j] != val:
                nums[i] = nums[j]
                nums[j] = val
        j = cycle_round - 1
        while j >= 0 and nums[j] == val:
            j -= 1
        return j + 1


# 这是一个很烂的答案，速度巨慢，虽然使用的空间比较小
# 并且第一次对于[1],1和[4,5]两种情况没有处理好
class Solution:
    def removeElement(self, nums, val):  # 事实上没有必要在意val的位置，直接向后找不是val的向前写就行,参考了精选的思路
        a, b = 0, 0
        cycle_round = len(nums)
        while b < cycle_round:
            if nums[b] != val:
                nums[a] = nums[b]
                a += 1
            b += 1
        return a


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement([4, 5], 4))
