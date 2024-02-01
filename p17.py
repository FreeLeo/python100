def select_sort(items, comp=lambda x, y: x < y):
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i+1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(items, comp=lambda x, y: x > y):
    for i in range(len(items)-1):
        swaped = False
        for j in range(len(items)-1-i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swaped = True
        if not swaped:
            break
    return items


def main():
    items = [3, 7, 1, 9, 0]
    items = bubble_sort(items)
    print(items)


if __name__ == '__main__':
    main()
