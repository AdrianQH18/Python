# Modifica el ejercicio anterior para que, nos muestre en que posición del array se
# encuentran el máximo y el mínimo. Si están repetidos y aparecen en mas de una
# posición debería de indicarlas todas
import random

n = int(input("Número de elementos: "))
array = [random.randint(10, 1000) for _ in range(n)]

print("Array:", array)

maximo = max(array)
minimo = min(array)

pos_max = [i for i, v in enumerate(array) if v == maximo]
pos_min = [i for i, v in enumerate(array) if v == minimo]

print("Máximo:", maximo, "en posiciones", pos_max)
print("Mínimo:", minimo, "en posiciones", pos_min)
