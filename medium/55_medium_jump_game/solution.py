# https://leetcode-cn.com/problems/jump-game/
from typing import List


class Solution:
    # 简单的动态规划
    # 跑的时候超时了
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(0, n - 1):
            for j in range(1, nums[i] + 1):  # 一开始没考虑i+j的范围
                if i + j >= n:
                    break
                elif dp[i + j]:
                    continue
                else:
                    dp[i + j] |= dp[i]
        return dp[n - 1]

    # 一开始是按照每个位置的数都做处理，思考后，如果在某个位置已经到达了的最远距离，
    # 之后的数位跳步到达不了那就没有必要处理，增加一个最远到达即可
    # 这个写法逻辑正确但是慢
    def canJump2(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        longest_reach = -1  # 目前最远可以跳到的位置
        for i in range(0, n - 1):
            if longest_reach == n - 1:
                break
            elif i + nums[i] <= longest_reach:  # 这个是增加判断减少不必要的
                continue
            else:
                for j in range(longest_reach + 1, nums[i] + i + 1):  # 一开始忘记考虑循环不包含最后一个数字
                    # if j < n:
                    #     dp[j] |= dp[i]
                    # if dp[j]:
                    #     longest_reach = j
                    # 上面的写法会访问溢出
                    if j < n:
                        dp[j] |= dp[i]
                        if dp[j]:
                            longest_reach = j
                    else:
                        break
        return dp[n - 1]

    # 根本不需要dp数组，只需要维护一个最远到达，只要最远到达大于n-1就可以返回True
    # 有逻辑错误，更新第四版。逻辑错误为，假设i点根本不能到达，循环时也会到达
    def canJump3(self, nums: List[int]) -> bool:
        if not nums:
            return False
        longest_reach = 0
        n = len(nums)
        # 下面这个if用于长度为一的特殊情况，一开始没想起来，在第四版中去掉了，其实也可以不用
        if n == 1:
            return True
        for i in range(n - 1):
            if longest_reach >= n - 1:
                return True
            elif nums[i]:
                if nums[i] + i > longest_reach:
                    longest_reach = nums[i] + i
            else:
                continue
        return False

    def canJump4(self, nums: List[int]) -> bool:
        if not nums:
            return False
        longest_reach = 0
        n = len(nums)
        for i in range(0, n - 1):
            if i <= longest_reach:
                if longest_reach >= n - 1:
                    break
                elif nums[i]:
                    if nums[i] + i > longest_reach:
                        longest_reach = nums[i] + i
                else:
                    continue
            else:
                break
        if longest_reach >= n - 1:
            return True
        else:
            return False

    def canJump5(self, nums: List[int]) -> bool:
        if not nums:
            return False
        longest_reach = 0
        for i, step in enumerate(nums):
            # if i <= longest_reach < i + step:
            # 上面这样的判断条件，遇到[3,0,8,2,0,0,1]出错
            if i <= longest_reach:
                if longest_reach < i + step:
                    longest_reach = i + step
            else:
                break
        return longest_reach >= len(nums) - 1


if __name__ == '__main__':
    sol = Solution()
    test_set = [
        [[2, 3, 1, 1, 4], True],
        [[3, 2, 1, 0, 4], False]
    ]
    for x, y in test_set:
        if sol.canJump5(x) == y:
            print('right')
        else:
            print('wrong')
