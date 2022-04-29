# https://leetcode-cn.com/problems/zigzag-conversion/
# 2022-04-25


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        tmp_result_list = [''] * numRows
        mod_num = numRows * 2 - 2
        for i, char in enumerate(s):
            # 位置换算公式
            x = i % mod_num
            index = min(x, (mod_num - x))
            tmp_result_list[index] += char
        return ''.join(tmp_result_list)


if __name__ == '__main__':
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
