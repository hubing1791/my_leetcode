# 暴力解法
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        num_stop = len(nums)
        while i < num_stop:
            j = i + 1
            for k in range(j, num_stop):
                if nums[i] + nums[k] == target:
                    break  # 其实可以直接return
            else:
                i = i + 1
                continue  # 跳出双重循环的写法
            break
        return [i, k]
