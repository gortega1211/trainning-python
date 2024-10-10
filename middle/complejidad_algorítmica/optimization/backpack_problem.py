"""
    RETOS
    - Poner print statements para ver que está pasando
    - Analizar complejidad algorítmica de la función recursiva
"""

def backpack(size_backpack, weigths, values, n):
    if n == 0 or size_backpack == 0:
        return 0
    
    if weigths[n - 1] > size_backpack:
        return backpack(size_backpack, weigths, values, n - 1)

    return max(values[n - 1] + backpack(size_backpack - weigths[n - 1], weigths, values, n - 1),
        backpack(size_backpack, weigths, values, n - 1))

if __name__ == '__main__':
    values = [60, 100, 120]
    weigths = [10, 20, 30]
    size_backpack = 30
    n = len(values)

    result = backpack(size_backpack, weigths, values, n)
    print(result)