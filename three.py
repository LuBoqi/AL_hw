# 定义一个Element类，用来存储元素的值和索引
class Element:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

    # 重写__lt__方法，比较两个元素的值和索引
    def __lt__(self, other):
        if self.val < other.val:
            return True
        elif self.val == other.val and self.idx > other.idx:
            return True
        return False


if __name__ == '__main__':
    # 输入一个字符串，将其转换为列表
    num = input('please input number:')
    k = eval(input('please input k:'))
    num_list = []
    # 将字符串转换为列表，并将其中的元素添加到num_list中
    for i, element in enumerate(num):
        num_list.append(Element(element, i))
    # 如果k大于数字的长度，则报错
    if k > len(num_list):
        print('k is too big')
        exit(0)
    # 将num_list中的元素按照val和idx的值进行排序
    num_list = sorted(num_list, reverse=True)
    # 删除num_list中k个元素
    num_list = num_list[k:]
    # 将num_list中的元素按照idx重新排序
    num_list = sorted(num_list, key=lambda x: x.idx)
    # 输出结果
    print('the answer is:', end='')
    for element in num_list:
        print(element.val, end='')
