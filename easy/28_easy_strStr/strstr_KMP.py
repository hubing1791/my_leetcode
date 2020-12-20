class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        elif len(haystack) < len(needle):
            return -1
        # 处理特殊情况

        next_needle = list(range(len(needle)))
        next_needle[0] = -1
        if len(needle) >= 2:
            next_needle[1] = 0
        index_max = len(needle)
        i, j = 1, 0
        while i < index_max - 1:
            if j == -1 or needle[j] == needle[i]:
                i += 1
                j += 1
                next_needle[i] = j
            else:
                j = next_needle[j]
        # 生成next数组
        i, j, index_max, needle_num = 0, 0, len(haystack), len(needle) - 1
        while i < index_max:
            if haystack[i] == needle[j]:
                if j == needle_num:
                    return i - j
                else:
                    i += 1
                    j += 1
            elif j == 0:
                i += 1
            else:
                j = next_needle[j]
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr("aaabaaabbbabaa","babb"))
