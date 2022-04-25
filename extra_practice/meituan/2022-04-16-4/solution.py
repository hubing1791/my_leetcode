# 没有100%过
def magic(x, y):
    tmp_count = 0
    while 1:
        if y // x >= 2:
            y = y // 2
            tmp_count += 1
        else:
            break
    return min((y - x), (x - (y // 2))) + tmp_count


if __name__ == "__main__":
    input_str = input().split()
    x = int(input_str[0])
    y = int(input_str[1])
    if x > y:
        x, y = y, x
    print(magic(x, y))