# 有一次提交错误，因为把字典初始值设置为了{'{': ' ', '}': '{','(': ' ', ')': '(','[': ' ', ']': '['}
# 这样无论括号进去的顺序如何，例如][显然不匹配，但是依旧可以通过
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = \
            {'{': ' ', '}': '{',
             '(': ' ', ')': '(',
             '[': ' ', ']': '['}
        stack_parentheses = ['']
        cycle_round = len(s)
        stack_pointer = 0
        for i in range(cycle_round):
            if parentheses_dict[s[i]] == stack_parentheses[stack_pointer]:
                stack_pointer -= 1
            else:
                stack_pointer += 1
                if len(stack_parentheses) < stack_pointer + 1:
                    stack_parentheses.append(s[i])
                else:
                    stack_parentheses[stack_pointer] = s[i]
        return stack_parentheses[stack_pointer] == ''


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("{[]}"))
