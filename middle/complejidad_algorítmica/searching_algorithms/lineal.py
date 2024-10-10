import random

def lineal_search(item_list, target):
    match = False

    for item in item_list: # O(n)
        if item == target:
            match = True
            break
    
    return match

if __name__ == '__main__':
    size_list = int(input('What size is the list?: '))
    target = int(input('What number do you want to find?: '))

    item_list = [random.randint(0, 100) for i in range(size_list)]

    found = lineal_search(item_list, target)
    print(item_list)
    print(f'The number {target} {"is" if found else "is not"} in the list')