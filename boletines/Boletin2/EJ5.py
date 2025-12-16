"""
5. Escribir un programa que nos pida las notas obtenidas en un trimestre y nos muestre
la media ponderada sabiendo que;
    1. La primera nota corresponde al trabajo en clase y cuenta como un 5% del total
    2. La segunda corresponde a los ejercicios prácticos: 15%
    3. La tercera la nota del examen: 80%
El resultado debería de mostrarse de dos formas: redondeado con dos decimales
(nota real) y sin redpmdeada sin decimales (nota de boletín).
"""

trabajo=float(input("Ingrese la nota de trabajo en clase: "))
ejercicios=float(input("Ingrese la nota de Ejercicios practicos: "))
examen=float(input("Ingrese la nota de Examen: "))

notaReal=(trabajo*0.05)+(ejercicios*0.15)+(examen*0.80)
print("Nota real: ",round(notaReal,2))
print("Boletin: ",int(notaReal))