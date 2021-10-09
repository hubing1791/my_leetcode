# https://leetcode-cn.com/problems/valid-palindrome/
# 2021-10-01

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 两边寻找，相遇即停止，发现冲突也直接返回false
        left, right = 0, len(s) - 1
        while left < right:
            while not (48 <= ord(s[left]) <= 57 or 65 <= ord(s[left]) <= 90 or 97 <= ord(s[left]) < 122):
                left += 1
            while not (48 <= ord(s[right]) <= 57 or 65 <= ord(s[right]) <= 90 or 97 <= ord(s[right]) < 122):
                right -= 1
            if left < right:
                if abs(ord(s[left]) - ord(s[right])) == 32 or ord(s[left]) - ord(s[right]) == 0:
                    left += 1
                    right -= 1
                else:
                    return False
        return True


if __name__ == "__main__":
    print(ord('A'), ord('Z'), ord('a'), ord('z'), ord('0'), ord('9'))
