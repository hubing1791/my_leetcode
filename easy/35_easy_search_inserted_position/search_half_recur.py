# nums如果是单列表或者空列表，search_half_recur无法正常运行
class Solution:
    def search_half_recur(self, nums, a, b, target):
        if b - a == 1 and nums[a] < target <= nums[b]:
            return b
        elif b - a == 1 and target <= nums[a]:
            return a
        elif b - a == 1 and target > nums[b]:
            return b + 1
        temp_med = (a + b) // 2
        if nums[temp_med] >= target:
            c = self.search_half_recur(nums, a, temp_med, target)
        else:
            c = self.search_half_recur(nums, temp_med, b, target)
        return c

    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums >= target:
                return 0
            else:
                return 1
        return self.search_half_recur(nums, 0, len(nums) - 1, target)


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 7))
