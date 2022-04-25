from typing import List


class Solution:
    def sol(self, a, b, father_list: List[int], value_list: List[int]):
        # 找到一个点的父亲及其祖先
        def find_fathers(x: int):
            tmp_result = [x]
            if x == 1:
                return tmp_result
            else:
                # 节点的父亲信息对应的下标为节点编号-2
                temp = x - 2
                while 1:
                    tmp_result.insert(0,father_list[temp])
                    temp = father_list[temp] - 2
                    if temp < 0:
                        break
            return tmp_result

        ans_a = find_fathers(a)
        ans_b = find_fathers(b)
        print(ans_a, ans_b)
        # 找到最近的公共祖先
        min_f = 0
        for i in range(min(len(ans_a), len(ans_b))):
            if ans_a[i] == ans_b[i]:
                min_f = i
            else:
                break
        node_min_road = ans_a[min_f:] + ans_b[min_f + 1:]
        print(node_min_road)
        result = node_min_road[0]
        for x in node_min_road[1:]:
            result ^= x
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.sol(3, 4, [1, 1, 2, 2, 3], [4, 3, 2, 1, 2, 1]))
