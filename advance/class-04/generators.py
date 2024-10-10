import time

def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if not max or n1 + n2 <= max:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                res = n1 + n2
                n1, n2 = n2, res
                counter += 1
                yield res
        else:
            break

if __name__ == "__main__":
    fibonacci = fibo_gen(55)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)