import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    list01 = list(map(int, list(sys.stdin.readline().strip())))
    if n == 1:
        print(1)
        exit()
    w, v = 0, 0
    for i in range(n):
        if list01[i] == 1:
            v += i + 1

    last_result = w - v
    for i in range( n):
        if list01[i]:
            v -= (i + 1)
        else:
            w += (i + 1)
        temp_result = w - v
        if last_result <= 0 and temp_result >= 0:
            print(min(abs(last_result), abs(temp_result)))
            exit()
        else:
            last_result = temp_result
