
class Solution:
    def count(self,str):
        count_num = 0
        for i in str:
            if i == ' ':
                count_num += 1
        return count_num


if __name__ == '__main__':
    str_test = input()
    sol = Solution()
    print(sol.count(str_test))