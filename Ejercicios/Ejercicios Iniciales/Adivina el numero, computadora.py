import random

def adivina_el_numero_com (x):
    print("Bienvenido al juego")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo")

    limite_inferior=1
    limite_superior=x

    respuesta = ""

    while respuesta != "c" :
        if limite_inferior != limite_superior:
            prediccion=random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #Puede ser el superior
        respuesta=input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, Ingresa (B). Si es correcto ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion -1
        elif respuesta == "b":
            limite_inferior = prediccion +1
    print(f"¡Felicidades! la computadora adivino tu numero correctamente {prediccion}.")
adivina_el_numero_com(10)