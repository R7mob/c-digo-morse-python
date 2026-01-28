import time
import os

# =========================
# DICIONÁRIO MORSE
# =========================

morse = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',
    'e': '.',     'f': '..-.',  'g': '--.',   'h': '....',
    'i': '..',    'j': '.---',  'k': '-.-',   'l': '.-..',
    'm': '--',    'n': '-.',    'o': '---',   'p': '.--.',
    'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',
    'y': '-.--',  'z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    ' ': '/'
}

# =========================
# DICIONÁRIO MORSE INVERTIDO
# =========================

morse_invertido = {}

for letra in morse:
    codigo = morse[letra]
    morse_invertido[codigo] = letra


# =========================
# TEXTO → MORSE
# =========================

def texto_para_morse(texto):
    resultado = ""

    for letra in texto:
        if letra in morse:
            resultado = resultado + morse[letra] + " "

    return resultado.strip()


# =========================
# MORSE → TEXTO
# =========================

def morse_para_texto(morse_texto):
    resultado = ""
    codigos = morse_texto.split(" ")

    for codigo in codigos:
        if codigo == "":
            continue
        elif codigo == "/":
            resultado = resultado + " "
        elif codigo in morse_invertido:
            resultado = resultado + morse_invertido[codigo]

    return resultado


# =========================
# MENU
# =========================

while True:
    print("\n1 - Texto para Morse")
    print("2 - Morse para Texto")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        texto = input("Digite o texto: ").lower()
        print("Morse:", texto_para_morse(texto))

    elif opcao == "2":
        texto = input("Digite o código Morse: ")
        print("Texto:", morse_para_texto(texto))

    elif opcao == "3":
        print("Saindo", end="", flush=True)
        for i in range(3):
            time.sleep(0.5)
            print('.', end="", flush=True)
        print() 
        time.sleep(0.3)
        os.system('cls')   
        break

    else:
        print("Opção inválida")