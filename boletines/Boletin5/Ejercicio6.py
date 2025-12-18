# 6. Escribe un programa que nos permita contar el número de veces que se repite cada
# cifra en un número. Por ejemplo, el número 885210003 tiene tres 0, un 1, un 2, un 5 y
# dos 8.

numero = input("Ejercicio 6: Inserte un número: ")
cifras = []

for i in numero:
    if i not in cifras:
        total = numero.count(i)
        print(f" El numero de veces que a salido {i} son {total}")
        cifras.append(i)