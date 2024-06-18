"""
Tipos de parámetros de una función:
- obligatorios
- opcionales
- una tupla: *args
- un diccionarios: **kwargs

Tipos anotados
"""


def sumar(a: str, b: str) -> str:
    return a + b

def funcion(ob, op=0, *args, **kwargs):
    print('obligatorio: ', ob)
    print('opcional:', op)
    print('args: ', args)
    print('kwargs: ', kwargs)
    print()


funcion(1)
funcion(1,2,3,4,5, x=10, y=20)
exit()
print(sumar("hola", "adios"))
print(sumar(12, 34))


