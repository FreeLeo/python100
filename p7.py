# 字符串和常用数据结构
# str2 = 'abc123'
# print(str2[-2])
# print(str2[-2::-1])
# print(str2[2::-1])
# print(str2[0::-1])
# print(str2.center(9, '*'))
# print(str2.rjust(9, '*'))
# print(str2.ljust(9, '*'))

# list1 = ['hello', 'lizhen', "apple", "world"]
# list1.append('append')
# list1.insert(1, "insert")
# list1 += ["aaaa", "bbbb"]
# list1.remove('lizhen')
# list2 = sorted(list1, key=len)
# list1.sort()
# for index in range(len(list1)):
#     print(index)
# for element in list1:
#     print(element)
# for index, element in enumerate(list1):
#     print(f"{index}, {element}")


# import sys


# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# print(sys.getsizeof(f))
# f = (x + y for x in 'ABCDE' for y in '1234567')
# print(sys.getsizeof(f))
# print(f)
# for val in f:
#     print(val)


# set1 = {3, 6, 1, 5, 8}
# set1.add(88)
# set1.update([11, 22])
# set1.discard(111)
# set1.remove(3)
# set1.pop()
# print(set1)


import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
