# https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
# 2022-05-05

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        length = len(s)
        left, right = 0, 0
        result = 0
        while right < length:
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            right += 1
            result = max(result, right - left)
        return result
