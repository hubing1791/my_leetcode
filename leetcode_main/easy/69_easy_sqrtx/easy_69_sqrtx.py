class Solution:
    def mySqrt_bin_as(self, left, right, x):
        if left == right:
            return left
        medium_num = (left + right) // 2
        if medium_num * medium_num >= x:
            result = self.mySqrt_bin_as(left, medium_num,x)
        else:
            result = self.mySqrt_bin_as(medium_num + 1, right, x)
        return result

    def mySqrt(self, x):
        result = self.mySqrt_bin_as(0, x, x)
        if result*result> x:
            return result-1
        else:
            return result