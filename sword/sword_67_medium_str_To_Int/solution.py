# https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/
# 2022-05-07

class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        # 有符号则从第二个人字符开始遍历
        result, index, sign = 0, 1, 1
        # 加减运算优先于移位运算，需要括号
        int_max, int_min, boundary = (1 << 31) - 1, -(1 << 31), (2 << 31) // 10
        if str[0] == '-':
            sign = -1
        elif str[0] != '+':
            index = 0
        for cha in str[index:]:
            if not '0' <= cha <= '9':
                break
            if result > boundary or result == boundary and cha > '7':
                if sign == 1:
                    return int_max
                else:
                    return int_min
            result = result * 10 + ord(cha) - ord('0')
        return sign * result


if __name__ == '__main__':
    so = Solution()
    print(so.strToInt("2147483648"))
