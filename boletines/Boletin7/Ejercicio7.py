# Pide al usuario un número y crea un array de enteros de tantas posiciones como indique
# ese número. Rellénalo con números aleatorios entre el 10 y el 1000 y finalmente
# pregunta al usuario por la posición de la que quiere recuperar el valor. El programa
# mostrará el número de la posición indicada si esta existe y un error si tratamos de
# recuperar una posición que no existe (menor a 0 o mayor a la longitud del array

import random

n = int(input("Número de elementos: "))
array = [random.randint(10, 1000) for _ in range(n)]

print("Array:", array)

pos = int(input("Introduce la posición a consultar: "))

if 0 <= pos < len(array):
    print("Valor:", array[pos])
else:
    print("Error: posición fuera del array")
