"""
Definición de funciones
"""
import math
import conversor

def ecuacion(a,b,c):
    raiz = b**2 - 4*a*c
    if raiz > 0:
        x1 = (-b + math.sqrt(raiz)) / (2*a)
        x2 = (-b - math.sqrt(raiz)) / (2*a)
        return x1, x2
    else:
        return None


def csvTojson(csv, sep=";"):
    # Convertir CSV a Lista de diccionarios:
    L = csv.split("\n")
    R = list()
    cabs = L[0].split(sep)
    for linea in L[1:]:
        datos = linea.split(sep)
        d = dict(zip(cabs, datos))
        # print(d)
        R.append(d)
    return R


def jsonTocsv():
    pass


if __name__ == "__main__":
    # Prueba de la ecuacion
    resul = ecuacion(1,5,4)
    if resul:
        x1, x2 = resul
        print(x1, x2)
    else:
        print('No hay solución')

    # csv to json:
    R = csvTojson(conversor.csv)
    print(R[:2])
