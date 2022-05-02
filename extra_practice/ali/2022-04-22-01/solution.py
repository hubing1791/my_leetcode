import sys
from typing import List


def color(x, y, clist: List):
    x_max = x
    y_max = y
    martix = [['.'] * y for _ in range(x)]

    def helper(char_c, x_loc, y_loc):
        move = [
            [-2, 0], [-1, 0], [0, 0], [2, 0], [1, 0]
            , [0, -2], [0, -1], [0, 1], [0, 2]
        ]
        for mov_x, mov_y in move:
            tmp_x, tmp_y = x_loc + mov_x, y_loc + mov_y
            if 0 <= tmp_x < x_max and 0 <= tmp_y < y_max:
                martix[tmp_x][tmp_y] = char_c

    for a, b, c in clist:
        helper(c, a, b)
    for str_r in martix:
        print(''.join(str_r))


if __name__ == '__main__':
    n, m, k = list(map(int, sys.stdin.readline().strip().split()))
    c_list = []
    for i in range(k):
        in_list = sys.stdin.readline().strip().split()
        x_in, y_in, char_in = int(in_list[0]) - 1, int(in_list[1]) - 1, str(in_list[2])
        c_list.append([x_in, y_in, char_in])
    color(n, m, c_list)
