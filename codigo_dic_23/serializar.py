"""
Serializar un lista de objetos y deserializar
"""
import pickle as p
from objetos import Persona
from random import randint


def serializar(path, L):
    pass


def deserializar(path):
    pass


def generarLista():
    L = []
    for i in range(65, 65 + 26):
        p = Persona(chr(i) * 3, randint(18, 65), randint(160, 190) / 100)
        L.append(p)
    return L


if __name__ == "__main__":
    L = generarLista()
    serializar("personas.dat", L)
    L2 = deserializar("personas.dat")
    for p in L2:
        print(p)
