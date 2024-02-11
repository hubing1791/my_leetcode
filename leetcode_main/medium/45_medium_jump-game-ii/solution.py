# https://leetcode.cn/problems/jump-game-ii/
# 2024-02-11
from typing import List

class Solution:
    # this solution will run out of time 
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        result = [length]*length
        result[0] = 0
        for i in range(len(nums)):
            end_point = i+nums[i]+1
            for j in range(1,min(end_point,length)):
                # 这个减少循环的条件不足以解决timeout
                if end_point >= length:
                    return result[i]+1
                result[j] = min(result[j],result[i]+1)
        return result[-1]
    
    def jump1(self, nums: List[int]) -> int:
        end_point,max_positon,ans = 0,0,0
        target = len(nums)-1
        for i in range(target):
            max_positon = max(nums[i]+i,max_positon)
            if max_positon>=target:
                return ans + 1
            if end_point == i:
                ans +=1
                end_point = max_positon
        return ans

            

if __name__ == "__main__":
    sol = Solution()
    sol.jump([2,3,1,1,4])