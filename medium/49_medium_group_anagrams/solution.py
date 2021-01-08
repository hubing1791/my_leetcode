# https://leetcode-cn.com/problems/group-anagrams/
from typing import List
from collections import defaultdict


class Solution:
    # 一开始想先把字符串转化为集合，形成一个字符串集合列表，但是对于teek类的词无法解决
    # 参考了答案 https://leetcode-cn.com/problems/group-anagrams/solution/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        for ana_str in strs:
            count_list = [0] * 26
            for ch in ana_str:
                count_list[ord(ch) - ord('a')] += 1
            ana_dict[tuple(count_list)].append(ana_str)
        return list(ana_dict.values())


if __name__ == '__main__':
    test_set = [
        [
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
        ]
    ]
    sol = Solution()
    for x, y in test_set:
        print(str(sol.groupAnagrams(x)) + '\t' + str(y))
