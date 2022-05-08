# https://leetcode-cn.com/problems/compress-string-lcci/
# 2022-05-07

class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S
        tmp_char = ''
        count = 0
        result = ''
        for i in range(len(S)):

            if count == 0:
                tmp_char = S[i]
                count = 1
            else:
                if S[i] == tmp_char:
                    count += 1
                else:
                    result = result + tmp_char + str(count)
                    tmp_char = S[i]
                    count = 1
        # 最后一定有个结尾没处理
        result = result + tmp_char + str(count)
        return result if len(result) < len(S) else S
