# Incluye operaciones adicionales (raiz cuadrada, cuadrado, cubo, por ejemplo

import math

num = float(input("Introduce un número: "))
op = input("Operación (R=raíz, C=cuadrado, U=cubo): ").upper()

match op:
    case "R":
        print("Raíz cuadrada:", math.sqrt(num))
    case "C":
        print("Cuadrado:", num ** 2)
    case "U":
        print("Cubo:", num ** 3)
    case _:
        print("Operación no válida")
