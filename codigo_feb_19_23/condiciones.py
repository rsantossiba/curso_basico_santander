"""
A partir de dos números calcular el menor
"""

n1 = 46
n2 = 23

if n1 < n2:
    print(f"El menor es {n1}")

elif n1 == n2:
    print("Los valores son iguales")

else:
    print(f"El menor es {n2}")

# Comprobar si una variable se encuentra dentro
# un intervalo:
ini = 10
fin = 40
num = 11
if num >= ini and num <= fin:
    print("dentro del intervalo")
else:
    print("fuera del intervalo")

if ini <= num <= fin:
    print("dentro del intervalo")
else:
    print("fuera del intervalo")

if num < ini or num > fin:
    print("fuera del intervalo")
else:
    print("dentro del intervalo")

if not (num >= ini and num <= fin):
    print("fuera del intervalo")
else:
    print("dentro del intervalo")
