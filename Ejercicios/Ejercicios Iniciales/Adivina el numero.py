import random


def adivina_el_numero (x):
    print("Adivina el Número")
    print("Tu meta es adivinar el numero generado por la computadora")
    numero_aleatorio = random.randint(1, x) #Numero aleatorio entre 1 y x.}
    prediccion = 0
    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adiviná un número entre 1 y {x}: "))
        if prediccion < numero_aleatorio :
            print("El número es muy chico")
        elif prediccion > numero_aleatorio :
            print("El número es muy grande")
    print(f"¡Felicitaciones! Adivinaste el número {numero_aleatorio} correctamente")
adivina_el_numero (10)