# 利用zip函数解决,速度没我的快但是优雅
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        result = ''
        strs_reverse = list(zip(*strs))
        for set_temp in strs_reverse:
            if len(set(set_temp)) == 1:
                result += set_temp[0]
            else:
                break
        return result


if __name__ == '__main__':
    strs_1 = ["flower", "flow", "flight"]
    strs_2 = ["dog", "racecar", "car"]
    print(list(zip(*strs_1)))
    print(list(zip(*strs_2)))
