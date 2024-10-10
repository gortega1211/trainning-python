import random

def bubble_sort(item_list):
    n = len(item_list)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if item_list[j] > item_list[j + 1]:
                item_list[j], item_list[j + 1] = item_list[j + 1], item_list[j]

    return item_list

if __name__ == '__main__':
    size_list = int(input('What size is the list?: '))

    item_list = [random.randint(0, 100) for i in range(size_list)]
    print(item_list)

    sorted_list = bubble_sort(item_list)
    print(sorted_list)