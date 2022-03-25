# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/
# 2022-03-02


class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 如果除尽则直接返回整数的结果
        if numerator % denominator == 0:
            return str(numerator // denominator)

        result = ''

        # 处理整数部分
        # 先判断结果的符号,这么写就是结果比较，意味着两者不同号
        if (numerator < 0) != (denominator < 0):
            result += '-'
        numerator, denominator = abs(numerator), abs(denominator)
        remainder = numerator % denominator
        result += str(numerator // denominator) + '.'

        # 处理小数部分
        # 答案用字典不用set是因为需要保留顺序，set是直接hash存储的，但是经过思考，可以使用（这个思路是第一版的，不对）
        # 有问题，并不是所有的小数部分都是循环节。
        index_map = dict()
        cycle_number = 0
        decimal_str = ''
        while remainder and remainder not in index_map:
            index_map[remainder] = cycle_number
            decimal_str += str((remainder * 10) // denominator)
            remainder = (remainder * 10) % denominator
            cycle_number += 1
        if remainder:
            # 取出需要切开的位置
            index_loc = index_map[remainder]
            decimal_str = decimal_str[:index_loc] + '(' + decimal_str[index_loc:] + ')'
            result += decimal_str
        else:
            result += decimal_str
        return result


if __name__ == "__main__":
    sol = Solution()
    test_set = [[1, 6],
                [4,333]
                ]
    for x, y in test_set:
        print(sol.fractionToDecimal(x, y))
