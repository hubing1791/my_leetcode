class Solution:
    def time_count(self, list1, list2):
        hour_dis = int(list2[0]) - int(list1[0])
        min2 = int(list2[1])
        min1 = int(list1[1])
        return hour_dis * 60 + min2 - min1


if __name__ == "__main__":
    list1_str = input()
    list2_str = input()
    list1_str = list1_str.split()
    list2_str = list2_str.split()
    sol = Solution()
    print(sol.time_count(list1_str,list2_str))