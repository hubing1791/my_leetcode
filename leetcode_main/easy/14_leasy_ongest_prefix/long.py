# 一开始没有考虑空列表输入
# 别人的解析有利用字典序的，非常值得学习
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strnum = len(strs)
        if strnum == 0:
            return ''  # 排除空列表
        flag = 1
        for word in strs:
            if flag:
                len_min = len(word)
                flag = 0
            if len(word) < len_min:
                len_min = len(word)  # 找出最短的单词长度，防止之后索引访问溢出
        round = 0
        result = ''
        while round < len_min:
            temp_char = strs[0][round]
            for i in range(1, strnum, 1):
                if strs[i][round] != temp_char:
                    break
            else:
                result = result + temp_char
                round += 1
                continue
            break
        return result


if __name__ == '__main__':
    solong = Solution()
    print(solong.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solong.longestCommonPrefix(["dog", "racecar", "car"]))
