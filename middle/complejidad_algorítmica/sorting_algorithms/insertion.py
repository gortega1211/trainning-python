import random

def insertion_sort(item_list):

    for index in range(1, len(item_list)):
        actual_value = item_list[index]
        actual_position = index

        while actual_position > 0 and item_list[actual_position - 1] > actual_value:
            item_list[actual_position] = item_list[actual_position - 1]
            actual_position -= 1

        item_list[actual_position] = actual_value
        return item_list

if __name__ == '__main__':
    size_list = int(input('What size is the list?: '))

    item_list = [random.randint(0, 100) for i in range(size_list)]
    print(item_list)

    sorted_list = insertion_sort(item_list)
    print(sorted_list)