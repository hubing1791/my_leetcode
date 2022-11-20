# https://leetcode-cn.com/problems/first-bad-version/
# 2022-05-08

# The isBadVersion API is already defined for you.

def isBadVersion(version: int) -> bool:
    if version >= 4:
        return False
    else:
        return True


class Solution:
    # 这版错误在于，只有l的部分需要加一
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            med = (l + r) // 2
            med_bool = isBadVersion(med)
            if not med_bool:
                if med + 1 <= n and not isBadVersion(med + 1):
                    l = med + 1
                if med + 1 <= n and isBadVersion(med + 1):
                    return med + 1
            else:
                if med - 1 > 0 and isBadVersion(med - 1):
                    r = med - 1
                if med - 1 > 0 and not isBadVersion(med - 1):
                    return med - 1
        return l if isBadVersion(l) else l + 1

    def firstBadVersion1(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            med = (l + r) // 2
            med_bool = isBadVersion(med)
            if not med_bool:
                l = med + 1
            else:
                r = med
        return l


if __name__ == '__main__':
    so = Solution()
    so.firstBadVersion(5)
