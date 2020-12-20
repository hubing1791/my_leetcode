# 参考了官方思路:滑动窗口法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows_set = set()  # hash集合，存着已经出现的字符
        pointer_back, max_length = 0, 0
        index_num = len(s)
        for i in range(index_num):
            if i > 0:
                windows_set.remove(s[i - 1])  # 向后移动，去掉已经划过的元素
            while pointer_back < index_num and s[pointer_back] not in windows_set:
                windows_set.add(s[pointer_back])
                pointer_back += 1
            max_length = max(max_length, pointer_back - i)
        return max_length
