# 定义递归生成函数，参数分别为shedule，begin，end，min，max
def recursiveGenerate(shedule, begin, end, min, max):
    if end[0] - begin[0] == 1:  # 边界条件
        if end[1] - begin[1] == 0:
            shedule[begin[0]][begin[1]] = max
            shedule[end[0]][end[1]] = min
        elif end[1] - begin[1] == 1:
            shedule[begin[0]][begin[1]] = min
            shedule[begin[0]][end[1]] = max
            shedule[end[0]][begin[1]] = max
            shedule[end[0]][end[1]] = min
        return shedule
    # 左上部分
    recursiveGenerate(shedule, begin,
                      [(begin[0] + end[0]) // 2, (begin[1] + end[1] - 1) // 2],
                      min, (min + max) // 2)
    # 右上部分
    recursiveGenerate(shedule,
                      [begin[0], (begin[1] + end[1] + 1) // 2],
                      [(begin[0] + end[0]) // 2, end[1]],
                      (min + max + 1) // 2, max)
    # 左下部分
    recursiveGenerate(shedule, [(begin[0] + end[0] + 1) // 2, begin[1]],
                      [end[0], (begin[1] + end[1] - 1) // 2],
                      (min + max + 1) // 2, max)
    # 右下部分
    recursiveGenerate(shedule, [(begin[0] + end[0] + 1) // 2, (begin[1] + end[1] + 1) // 2],
                      end, min, (min + max) // 2)
    return shedule


# 定义生成函数，参数为p
def generateSchedule(p):
    # 计算m的值
    m = 2 ** p
    # 初始化shedule
    shedule = [[0 for x in range(m - 1)] for y in range(m)]
    # 调用递归生成函数
    shedule = recursiveGenerate(shedule, [0, 0], [m - 1, m - 2], 1, m)
    # 返回shedule
    return shedule


# 调用生成函数
if __name__ == '__main__':
    # 输入p的值
    p = eval(input('please in put p:'))
    # 调用生成函数
    ans = generateSchedule(p)
    # 遍历ans
    for line in ans:
        # 打印line
        print(line)
