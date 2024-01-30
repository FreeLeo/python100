# a = 100
# b = 12.34
# c = 1 + 5j
# d = 'hello'
# e = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))


# aa = int(input('aa = '))
# bb = int(input('bb = '))
# print(f"aa={aa}, bb={bb}, {aa}+{bb}={aa+bb}")


# F = float(input('F = '))
# C = (F - 32) / 1.8
# print(f"{F:.1f}华氏温度等于{C:.2f}摄氏温度。")


# radius = float(input('请输入半径：'))
# perimeter = 2 * 3.1416 * radius
# area = 3.1416 * radius * radius
# print(f"半径为{radius},周长为{perimeter:.2f},面积为{area:.2f}.")

year = int(input('请输入年份:'))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)
