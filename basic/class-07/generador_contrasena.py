import random

def generar_contrasena():
    mayusculas = [chr(i) for i in range(65, 91)]
    minusculas = [chr(i) for i in range(97, 123)]
    numeros = [chr(i) for i in range(48, 58)]
    simbolos = [chr(i) for i in range(33, 48)]

    caracteres = mayusculas + minusculas + numeros + simbolos

    contrasena = list()

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    nueva_contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + nueva_contrasena)

if __name__ == "__main__":
    run()
    