"""
POO en Python. Características:
- Soporta la sobrecarga de operadores: relacionales, aritméticos ...
- 
"""

from random import randint
from string import ascii_uppercase


def generarDatos():
    candidatos = [
        {
            "nombre": letra * 3,
            "años": randint(5, 10),
            "numempresas": randint(1, 8),
            "superior": True if randint(2, 10) % 2 == 0 else False,
        }
        for letra in ascii_uppercase
    ]
    return candidatos


class Candidato:
    """Implementación de la clase Candidato"""

    def __init__(self, nombre="", años=0, numempresas=0, superior=False):
        # Definir atributos:
        self.nombre = nombre
        self.años = años
        self.numempresas = numempresas
        self.superior = superior

    def actualizarExp(self):
        self.años += 1

    def __str__(self):
        return (
            self.nombre
            + " "
            + str(self.años)
            + " "
            + str(self.numempresas)
            + " "
            + str(self.superior)
        )

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        if self.años < other.años:
            return True

        elif self.años == other.años:
            if self.numempresas < other.numempresas:
                return True
            elif other.numempresas < self.numempresas:
                return False
            else:  # mismo numero de empresas
                if not self.superior:
                    return True
                else:
                    return False
        else:
            return False


if __name__ == "__main__":
    c1 = Candidato("Juan", 10, 5, True)
    c2 = Candidato("Pedro", 12, 5, False)
    print(c1)
    c1.actualizarExp()
    print(c1)
    # print(str(c1))
    # print(c1.__str__())
    L = [c1, c2]
    print(L)

    lista = generarDatos()
    L = [Candidato(**d) for d in lista]
    L.sort()
    L.sort(key=lambda x: x.años, reverse=True)
    for c in L:
        print(c)
