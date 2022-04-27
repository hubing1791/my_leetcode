# 2022-04-27
# 合并三个有序数组

class SB:
    def sorted_list_c(self, list_a, list_b, list_c):
        result = []
        leng_a, leng_b, leng_c = len(list_a), len(list_b), len(list_c)
        end = max(list_a[-1], list_b[-1], list_c[-1]) + 1
        # 这样直接解决溢出了
        list_a += [end]
        list_b += [end]
        list_c += [end]
        index_a, index_b, index_c = 0, 0, 0
        while index_a < leng_a or index_b < leng_b or index_c < leng_c:
            if list_a[index_a] <= list_b[index_b] and list_a[index_a] <= list_c[index_c]:
                result.append(list_a[index_a])
                index_a += 1
            if list_c[index_c] <= list_b[index_b] and list_a[index_a] >= list_c[index_c]:
                result.append(list_c[index_c])
                index_c += 1
            if list_c[index_c] >= list_b[index_b] and list_a[index_a] >= list_b[index_b]:
                result.append(list_b[index_b])
                index_b += 1
        return result[:-1]


if __name__ == '__main__':
    so = SB()
    print(so.sorted_list_c([1, 2, 3], [3, 6, 8], [1, 4, 9]))
