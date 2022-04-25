class Solution:
    def ti_count(self, num, list1, list2):
        pre_result = [0] * num
        length = len(list1)
        for i in range(length):
            for j in range(list1[i] - 1, list2[i]):
                pre_result[j] += 1
        result = 0
        for i in pre_result:
            if i >= 2:
                result += 1
        return result


if __name__ == "__main__":
    num = int(input().split()[0])
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    sol = Solution()
    print(sol.ti_count(num,list1,list2))