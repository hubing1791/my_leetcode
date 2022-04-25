import sys
from typing import List


def sort_num(n_list: List):
    length, width = len(n_list),len(n_list[0])
    str_relist = [""] * width
    for i in range(width):
        for j in range(length):
            str_relist[i] += n_list[j][i]
    for i in range(width):
        str_relist[i] = int(str_relist[i])
    str_relist.sort()
    result = " ".join(list(map(str,str_relist)))
    print(result)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    list_str = []
    for i in range(n):
        list_str.append(sys.stdin.readline().strip())
    print(list_str)
    sort_num(list_str)