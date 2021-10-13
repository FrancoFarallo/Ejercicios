import random

import string

from ahorcado_diagramas import vidas_diccionario_visual

from palabras1 import palabras


def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)
    
    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()


def ahorcado ():
    print("¡Bienvenido al Ahorcado!")
    
    
    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase) #No contiene la Ñ
    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0 :
        print(f"Te quedan {vidas} vidas y usaste estas letras: {''.join(letras_adivinadas)}")

        palabra_lista = [letra if letra in letras_adivinadas
        else "-" for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()
        #si la letra que eligio el usuario esta en el abecedario y no esta en el conjunto de letras ya ingresadas, se añade la letra al conjunto de ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(" ")
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra")
        elif letra_usuario in letras_adivinadas:
            print("\nYa eslegiste esa letra, por favor elegí una nueva")
        else:
            print("\nEsta letra no es válida.")
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Perdiste. La palabra era: {palabra}")
    else:
        print(f"¡Excelente! Adivinaste la palabra {palabra}")

ahorcado()