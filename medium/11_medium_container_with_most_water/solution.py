# 使用贪心算法，贪心算法正确性，
# 即为每次移动式扔掉的方案个数之和，
# 加上贪心算法n-1词的结果，正好是暴力方案数量
class Solution:
    def maxArea(self, height) -> int:
        index_left, index_right = 0, len(height) - 1
        water_max = 0
        while index_right > index_left:
            width = index_right - index_left
            height_temp = min(height[index_left], height[index_right])
            square = width * height_temp
            if square > water_max:
                water_max = square
            if height[index_left] >= height[index_right]:
                index_right -= 1
            else:
                index_left += 1
        return water_max
