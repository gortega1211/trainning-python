def divisors(num):
    divisors = list()
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Ingresa un número: ")
    assert num.isnumeric() and int(num) > 0, "Debe ingresar un número entero positivo"
    print(divisors(int(num)))
    print("Terminó mi programa")

if __name__ == "__main__":
    run()