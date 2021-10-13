from django.http import HttpResponse




adj= input("Adjetivo: ")
obj = input("Objeto, comida, etc.: ")
verbo=input("Verbo: ")
def texto (request):
    return HttpResponse (madlib)
madlib= f"Franco es tan {adj}, le encantan los {obj} y se la pasa {verbo}."
print (madlib)
def texto (request):
    return HttpResponse (print(madlib))