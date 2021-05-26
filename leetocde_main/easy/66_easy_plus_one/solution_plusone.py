# 这是来回转化类型的版本
class Solution:
    def plusOne(self, digits):
        result = ''
        for i in digits:
            result += str(i)
        result = int(result) + 1
        result = str(result)
        result_list = []
        for i in range(len(result)):
            result_list.append(int(result[i]))
        return result_list
