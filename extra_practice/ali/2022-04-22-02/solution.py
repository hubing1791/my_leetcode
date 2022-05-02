import sys


# 避免对7.0000.3这种切割错误即可
def cut(str_c: str):
    tem_result = []
    index = 0
    # 表示是否遇到.
    flag_dot = 0
    i = 0
    while i < len(str_c):
        if flag_dot == 0 and str_c[i] == '.':
            i += 2
            flag_dot = 1
            continue
        if flag_dot == 0:
            i += 1
        if flag_dot == 1:
            if str_c[i] == '.':
                tem_result.append(str_c[index:i - 1])
                index = i - 1
                i += 2
                continue
            # 小数点后遇到不等于0，就可以看看下一个
            if str_c[i] == '0':
                i += 1
                continue
            tem_result.append(str_c[index:i])
            index = i
            i += 1
            flag_dot = 0
    if index < len(str_c):
        tem_result.append(str_c[index:i])
    result = 0.0
    for x in tem_result:
        result += float(x)
    return result


if __name__ == '__main__':
    str_in = sys.stdin.readline().strip()
    print(cut(str_in))