import heapq
# 生成式的用法
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)


# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}的成绩'))
# print(scores)


# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(5, list1))
# print(heapq.nlargest(3, list2, key=lambda x: x['price']))
# print(heapq.nsmallest(3, list2, key=lambda x: x['name']))


# import itertools


# # 产生ABCD的全排列
# permutations = itertools.permutations('ABCD', r=2)
# print("全排列:")
# for perm in permutations:
#     print(''.join(perm))

# # 产生ABCDE的五选三组合
# combinations = itertools.combinations('ABCDE', 3)
# print("\n五选三组合:")
# for combo in combinations:
#     print(''.join(combo))

# # 产生ABCD和123的笛卡尔积
# product = itertools.product('ABCD', '123')
# print("\n笛卡尔积:")
# for item in product:
#     print(''.join(item))

# # 产生ABC的无限循环序列
# cycle = itertools.cycle(('A', 'B', 'C'))
# print("\n无限循环序列:")
# for _ in range(10):  # 打印前10个元素
#     print(next(cycle))


from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))
