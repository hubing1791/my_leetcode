# https://leetcode-cn.com/problems/longest-valid-parentheses/
class Solution:
    # 把有效的子串切割出来，最初做法不对，只能处理左括号比右括号多的情况，并且把失配的)也放进去了,
    # 然而还是不对，无法处理()(()这种的
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)  # 括号串的长度
        pre_pointer, back_pointer = 0, 0  # 两个指针之间夹的子串就是目前匹配出的子串
        result = []  # 储存子串
        stack = []  # 验证括号合法性的栈
        for i in range(n):
            back_pointer += 1
            if s[i] == '(':
                stack.append(s[i])
            else:
                if not stack:
                    result.append(s[pre_pointer:back_pointer - 1])
                    pre_pointer = back_pointer
                else:
                    char_temp = stack.pop()
                    if char_temp == ')':
                        result.append(s[pre_pointer:back_pointer - 1])
                        pre_pointer = back_pointer
                    else:
                        pass
        # 修改时多加了一个if判断，处理全部循环结束栈还没弹完的情况和栈全部弹完没遇到失配未放进result的情况
        if back_pointer - pre_pointer >= 2:
            result.append('*' * (back_pointer - pre_pointer - len(stack)))
        max_length = 0  # result数组里最长的子串长度
        result_substr = ''
        for i in result:
            if len(i) > max_length:
                result_substr = i
                max_length = len(i)
        return result_substr

    # 官方解法之贪心算法，从右往左遍历,再从右往左遍历
    def longestValidParentheses2(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0  # 匹配的左右括号数量
        max_length = 0
        for i in range(1, n + 1):
            if s[-i] == ')':
                right += 1
            else:
                left += 1
            if left > right:
                left, right = 0, 0
            elif left == right:
                if left * 2 > max_length:
                    max_length = left * 2
            else:
                pass
        left, right = 0, 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if right > left:
                left, right = 0, 0
            elif right == left:
                if right * 2 > max_length:
                    max_length = right * 2
            else:
                pass
        return max_length

    # 官方解答动态规划
    def longestValidParentheses3(self, s: str) -> int:
        max_length = 0
        dp = [0] * len(s)  # 加一因为在出现访问dp[-1]时不会产生问题
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = 2 + dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
                max_length = max(dp[i], max_length)
        return max_length


if __name__ == '__main__':
    sol = Solution()
    teststr_1 = ")()())"
    teststr_2 = "(()"
    print(sol.longestValidParentheses2(teststr_1))
    # print(sol.longestValidParentheses(teststr_1))
    # print(sol.longestValidParentheses(teststr_2))
    # print([1, 2, 3, 4][5:6])
