import random

def binary_search(item_list, start, end, target):
    print(f'Searching {target} between {item_list[start]} and {item_list[end - 1]}')
    if start > end:
        return False

    middle = (start + end) // 2

    if item_list[middle] == target:
        return True
    elif item_list[middle] < target:
        return binary_search(item_list, middle + 1, end, target)
    else:
        return binary_search(item_list, start, middle - 1, target)

if __name__ == '__main__':
    size_list = int(input('Whats size is the list?: '))
    target = int(input('What number do you find?: '))

    sorted_list = sorted([random.randint(0, 100) for i in range(size_list)])

    found = binary_search(sorted_list, 0, len(sorted_list), target)

    print(sorted_list)
    print(f'The element {target} {"is" if found else "is not"} in the list.')