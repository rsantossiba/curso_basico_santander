"""
Calcular una ecuación de 2 grado en Python
ax^2 + by + c = 0

x1 = -b + ...
x2 = -b - ... 
"""

import math

# Inicialización múltiple:
a,b,c = 1,5,4

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print("x1: ", x1, "x2: ", x2)