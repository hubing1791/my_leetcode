# https://leetcode-cn.com/problems/string-to-url-lcci/
# 2022-05-07

class Solution:
    # 不用现成函数，使用双指针
    # 有更多效果更好做法，比如直接拼字符串，再范围内哦那个replace，感觉不符合题意没用
    def replaceSpaces(self, S: str, length: int) -> str:
        s_list = list(S)
        index_left, index_right = length - 1, len(s_list) - 1
        while index_left >= 0:
            if s_list[index_left] == ' ':
                s_list[index_right - 2:index_right + 1] = '%20'
                index_right -= 3
            else:
                s_list[index_right] = s_list[index_left]
                index_right -= 1
            index_left -= 1
        return ''.join(s_list[index_right+1:])


if __name__ == '__main__':
    pass
