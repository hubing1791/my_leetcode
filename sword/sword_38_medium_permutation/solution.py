# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
# 2022-04-30
from collections import defaultdict
from typing import List


class Solution:
    # 对应官解，思路一样，但是是我自己的写法
    def permutation(self, s: str) -> List[str]:
        char_dict = defaultdict(int)
        count = 0
        for char in s:
            char_dict[char] += 1
            count += 1
        result_str = ''
        result = []

        def dfs():
            nonlocal count
            nonlocal result_str
            nonlocal result
            if count == 0:
                result.append(result_str)
                return
            for key in char_dict:
                if char_dict[key] > 0:
                    result_str = result_str + key
                    char_dict[key] -= 1
                    count -= 1
                    dfs()
                    count += 1
                    char_dict[key] += 1
                    result_str = result_str[:-1]

        dfs()
        return result

    # 官解2，利用下一个排列
    def permutation_off2(self, s: str) -> List[str]:
        result = []
        str_list = list(s)
        s_length = len(s)
        if s_length <= 1:
            return [s]

        def next_permutation():
            nonlocal str_list
            nonlocal s_length
            index = s_length - 1
            while index > 0:
                if str_list[index - 1] < str_list[index]:
                    index -= 1
                    break
                else:
                    index -= 1
            # 处理找到了的情况,在右边寻找更大的字符
            if str_list[index] < str_list[index + 1]:
                index_large = s_length
                while index_large > index:
                    index_large -= 1
                    if str_list[index_large] > str_list[index]:
                        str_list[index_large], str_list[index] = str_list[index], str_list[index_large]
                        left, right = index + 1, s_length - 1
                        while left < right:
                            str_list[left], str_list[right] = str_list[right], str_list[left]
                            left += 1
                            right -= 1
                        return ''.join(str_list)
            else:
                # 一开始没有反转，只是返回了str，导致永远卡在这一步
                str_list.reverse()
                return ''.join(str_list)
            # 应对全是一个字母的情况
            return ''.join(str_list)

        while 1:
            s_new = next_permutation()
            result.append(s_new)
            if s_new == s:
                break
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.permutation_off2('abc'))
