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


def generateSchedule(p):
    m = 2 ** p
    shedule = [[0 for x in range(m - 1)] for y in range(m)]
    shedule = recursiveGenerate(shedule, [0, 0], [m - 1, m - 2], 1, m)
    return shedule


if __name__ == '__main__':
    p = eval(input('please in put p:'))
    ans = generateSchedule(p)
    for line in ans:
        print(line)
