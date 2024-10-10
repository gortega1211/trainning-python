"""
    REGLAS:
    - Incorporar comprenhensions. (REALIZADO)
    - Incorporar Manejo de Errores. (REALIZADO)
    - Incorporar Manejo de Archivos. (REALIZADO)
    - Utilizar el archivo data.txt para obtener las palabras. (REALIZADO)

    AYUDAS Y PISTAS
    - Investigar la función enumerate. (REALIZADO)
    - Investigar el método get de los diccionarios. (REALIZADO)
    - La sentencia os.system("cls") -> Windows o os.system("cls") -> Unix, para limpiar la pantalla. (REALIZADO)
    
    MEJORAR EL JUEGO
    - Añadir sistema de puntos. (REALIZADO)
    - Dibuja al "ahorcado" en cada jugada con código ASCII. (REALIZADO)
    - Mejora la interfaz. (REALIZADO)
"""

import random
import os

points = 0
attemps = 0
hangman_tmpl = [
    "    _ _ _ _",
    "   |       |",
    "   |       ",
    "   |      ",
    "   |       ",
    "   |      ",
    "   |",
    "   |",
    "-------"
]

hangman = hangman_tmpl.copy()

def get_words():
    words = list()
    with open('./data.txt', 'r', encoding='utf-8') as f:
        words = [line.replace('\n', '').upper() for line in f]
    return words

def select_word(words):
    return words[random.randint(0, len(words) -1)]

def clear_console():
    os.system("cls")

def get_word_size(secret_word):
    return ["_" for _ in secret_word]

def show_discovered_word(discovered_word):
    for letter in discovered_word:
        print(letter, end="")

def verify_letter(letter, secret_word, discovered_word):
    global points
    global attemps
    global hangman
    if letter in secret_word:
        points += 10 if letter not in discovered_word else 0
        index =  secret_word.find(letter)
        while index >= 0:
            discovered_word[index] = secret_word[index]
            index += 1
            next_index = secret_word[index:].find(letter)
            index = next_index + index if next_index >= 0 else -1
    else:
        attemps += 1
        points -= 1 if points > 0 else 0
        match attemps:
            case 1:
                hangman[2] += "O"
            case 2:
                hangman[3] += "/"
            case 3:
                hangman[3] += "|"
            case 4:
                hangman[3] += "\\"
            case 5:
                hangman[4] += "|"
            case 6:
                hangman[5] += "/"
            case 7:
                hangman[5] += " \\"
    return discovered_word

def compare_words(discovered_word, secret_word):
    for i, l in enumerate(discovered_word):
        if secret_word[i] != l:
            return False
    return True

def draw_hangman():
    for line in hangman:
        print(line)

def show_interface(discovered_word):
    clear_console()
    print("HANGMAN GAME")
    print("=" * 20)
    print("Puntos:", points, "\n")
    draw_hangman()
    print()
    show_discovered_word(discovered_word)

def show_finish_game():
    clear_console()
    print("GRACIAS POR JUGAR 'HANGMAN GAME'")
    print("HAS LOGRADO ALCANZAR", points, "PUNTOS")

def reset_values():
    global hangman
    global attemps
    hangman = hangman_tmpl.copy()
    attemps = 0

def run():
    playing = True
    words = get_words()
    
    while playing:
        guess = True
        secret_word = select_word(words)
        discovered_word = get_word_size(secret_word)
        while attemps < 7 and guess:
            show_interface(discovered_word)
            try:
                letter = input("\nIngresa una letra: ")
                assert letter.isalpha(), "Ingrese una letra!"
                assert len(letter) == 1, "Ingrese solamente 1 letra!"
                letter = letter.upper()
                discovered_word = verify_letter(letter, secret_word, discovered_word)
                guess = not compare_words(discovered_word, secret_word)
            except AssertionError as ae:
                print("\nERROR: " + str(ae))
                input("\nPresione una letra para continuar...")
        clear_console()
        print("PERDISTE!") if attemps == 7 else print("GANASTE!")
        draw_hangman() if attemps == 7 else ''
        print("LA PALABRA A ENCONTRAR ERA '" + secret_word + "'")
        play_again = input("\nDeseas Jugar nuevamente? (S/N): ")
        playing = True if play_again.upper() == 'S' else False
        reset_values()
    show_finish_game()

if __name__ == "__main__":
    run()