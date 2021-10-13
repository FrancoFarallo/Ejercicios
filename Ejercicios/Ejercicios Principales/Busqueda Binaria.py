import random


#La lista debe estar en orden ascendente para implementar esta funcion
def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior= 0 #inicio de la lista
    if limite_superior is None:
        limite_superior = len(lista) - 1 #Final de la lista
    if limite_superior < limite_inferior:
        return -1
    punto_medio = (limite_inferior + limite_superior)//2
    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)


tamaño = 10000
conjunto_inicial = set()

while len(conjunto_inicial) < tamaño:
    conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
lista_ordenada = sorted(list(conjunto_inicial))

print(busqueda_binaria(lista_ordenada, objetivo= 1000))