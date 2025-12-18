# Pide al usuario un número y crea un array de enteros de tantas posiciones como indique
# ese número. Rellenalo con números aleatorios entre el 10 y el 1000 y finalmente
# muestra cual es el máximo, cual el mínimo y la media aritmética con dos decimales.
import random

n = int(input("Número de elementos: "))
array = [random.randint(10, 1000) for _ in range(n)]

print(array)
print("Máximo:", max(array))
print("Mínimo:", min(array))
print("Media:", round(sum(array) / len(array), 2))
