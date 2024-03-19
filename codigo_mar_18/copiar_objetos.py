"""
Copia de objetos mutables:
set, list, dict: Método copy
"""

L1 = [1, 2, 3, 4, 5, 6]
L2 = L1  # No es una copia, es una referencia.
L1[0] = 1000
print("L1: ", L1, id(L1))
print("L2: ", L2, id(L2))
