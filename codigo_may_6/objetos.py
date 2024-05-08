"""
POO en Python:
Diseño de clases
- Sobrecarga de operadores
- Funciones especiales 
- Listas de objetos
"""

from typing import Any


class Persona:
    """Implementación de la clase Persona"""

    def __init__(self, nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad

    def __str__(self):
        return self.nombre + " " + str(self.altura) + " " + str(self.edad)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.edad < other.edad

    def __eq__(self, other: object) -> bool:
        for k, v in self.__dict__.items():
            if k in other.__dict__:
                if v != other.__dict__[k]:
                    return False
            else:
                return False
        return True

    def __del__(self):
        pass
        # print('Se está borrando: ', self.nombre)


def pruebaPersona():
    p1 = Persona("Miguel", 34, 1.8)
    p3 = Persona("Miguel", 34, 1.8)
    p4 = Persona("Miguel", 34, 1.81)
    p2 = Persona("Eva", 44, 1.79)
    print(p1)
    # print(str(p1))
    # print(p1.__str__())

    L = [p1, p2, Persona("Jose", 15, 1.77)]
    print(L)

    print("La clase del objeto: ", p1.__class__.__name__)
    print("Dic:", p1.__dict__)
    p1.tno = 915674433
    p1.__dict__["movil"] = 678456788
    print("Dic:", p1.__dict__)

    L.sort(reverse=True)
    print(L)
    if p1 < p2:
        print(p1.nombre, "es menor que", p2.nombre)
    else:
        print(p2.nombre, "es menor que", p1.nombre)

    if p1 > p2:
        print(p1.nombre, "es mayor que", p2.nombre)
    else:
        print(p2.nombre, "es mayor que", p1.nombre)

    if p4 == p3:
        print("iguales")
    else:
        print("no iguales")


if __name__ == "__main__":
    pruebaPersona()
