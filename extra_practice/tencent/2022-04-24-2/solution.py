from typing import List


class Solution:
    # 这是初代版本
    def getNumber(self, a: List):
        # 判断是否是素数
        def is_p(num: int):
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    return False
            return True

        n = len(a)
        p_set = {2, 3}
        for i in range(3, n + 1):
            if i % 6 == 5 or i % 6 == 1:
                if is_p(i):
                    p_set.add(i)
        length = len(a)
        while length > 1:
            temp_list = []
            for i in range(length):
                if i + 1 in p_set:
                    temp_list.append(a[i])
            a = temp_list
            length = len(a)
        return a[0]

    # 找素数用埃拉托斯特尼筛法优化
    def getNumber_new(self, a: List):
        def fin_p(n: int):
            prime_list = [True]*(n+1)
            prime_list[:1] = [False,False]
            k = 2
            while k * k <= n:
                if prime_list[k]:
                    j = k * k
                    while j <= n:
                        prime_list[j] = False
                        j += k
                k+=1
            result = set()
            for i in range(n+1):
                if prime_list[i]:
                    result.add(i)
            return result
        p_set = fin_p(len(a))
        # print(p_set)
        length = len(a)
        while length > 1:
            temp_list = []
            for i in range(length):
                if i + 1 in p_set:
                    temp_list.append(a[i])
            a = temp_list
            length = len(a)
        return a[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.getNumber_new([3,1,1,4,5,6,1,1,1,1,1,1,1,1,1,1,1,1,1]))


