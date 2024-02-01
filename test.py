print(f"{2**3}")
print(f"{123 / 10}")
print(f"{123 // 10}")
print(f"{123 % 10}\\")

total = 0
print(f"{1 if 1 <= total else 0}")


def num_generator(m, n):
    return range(m, n+1)


for i in num_generator(1, 5):
    print(i)


def num_generator(m, n):
    yield from range(m, n+1)


for i in num_generator(1, 5):
    print(i)