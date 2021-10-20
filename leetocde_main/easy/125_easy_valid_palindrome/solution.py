# https://leetcode-cn.com/problems/valid-palindrome/
# 2021-10-01

class Solution:
    # python提供了isalnum()，lower()，不用像我这样写这么复杂的
    # 还有一种思路，先遍历并对字母都转小写，然后翻转一下，看是否相等
    def isPalindrome(self, s: str) -> bool:
        # 两边寻找，相遇即停止，发现冲突也直接返回false
        left, right = 0, len(s) - 1
        while left < right:
            # while里没有再判断一次left<right,会导致越界
            #
            while left < right and not (
                    48 <= ord(s[left]) <= 57 or 65 <= ord(s[left]) <= 90 or 97 <= ord(s[left]) <= 122):
                left += 1
            while left < right and not (
                    48 <= ord(s[right]) <= 57 or 65 <= ord(s[right]) <= 90 or 97 <= ord(s[right]) <= 122):
                 right -= 1
            if left < right:
                if (abs(ord(s[left]) - ord(s[right])) == 32 and ord(s[right]) > 64 and ord(s[left]) > 64) or (
                        ord(s[left]) - ord(s[right])) == 0:
                    left += 1
                    right -= 1
                else:
                    return False
        return True


if __name__ == "__main__":
    print(ord('0'),ord("9"),ord('a'),ord('z'),ord('A'),ord('Z'))
    sol = Solution()
    print(sol.isPalindrome("Zeus was deified, saw Suez."))
