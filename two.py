"""
    1）两台机器一起加工十个零件
    2）不同机器加工不同零件的时间不同
    3）求十个零件最短的加工时间

    a = [1   3 5 7 4 2 8 4  9 9]
    b = [1.5 2 6 8 2 1 3 8 11 4]
    当完成k个作业时，设机器A花费的时间为x，则机器B花费的时间的最小值为x的一个函数，
    设F[k,x]表示在完成k个作业时机器A花费时间x的条件下，机器B所花费时间的最小值
    递推式：F[k,x]= min {F[k-1,x]+ b[k] , F[k-1, x-a[k]]}
"""


def min_machineB_time(a, b):
    n = len(a)
    MAX_INT = float('inf')

    # 初始化二维数组dp
    dp = [[MAX_INT] * (sum(a) + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    # 备忘录存储A的加工顺序
    order = [[[] for _ in range(sum(a) + 1)] for _ in range(n + 1)]

    # 动态规划递推
    for k in range(1, n + 1):
        for x in range(sum(a) + 1):
            dp[k][x] = min(dp[k][x], dp[k - 1][x] + b[k - 1])
            order[k][x] = order[k - 1][x]
            if x >= a[k - 1]:
                if dp[k][x] > dp[k - 1][x - a[k - 1]]:
                    order[k][x] = order[k - 1][x - a[k - 1]] + [k]
                dp[k][x] = min(dp[k][x], dp[k - 1][x - a[k - 1]])

    # 找到最小花费时间
    min_time = float('inf')
    idx = 0
    for x in range(sum(a) + 1):
        if max(dp[n][x], x) < min_time:
            min_time = max(dp[n][x], x)
            idx = x
    orderB = [x for x in range(1, n + 1) if x not in order[n][idx]]
    return min_time, order[n][idx], orderB


a = [1, 3, 5, 7, 4, 2, 8, 4, 9, 9]  # 机器A花费时间
b = [1.5, 2, 6, 8, 2, 1, 3, 8, 11, 4]  # 机器B花费时间
# a = [1, 3]  # 机器A花费时间
# b = [1.5, 2]  # 机器B花费时间

result = min_machineB_time(a, b)
print("花费时间的最小值:", result[0])
print("A的加工顺序：", result[1])
print("B的加工顺序：", result[2])
