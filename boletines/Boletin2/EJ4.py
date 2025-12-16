"""
4. Escribir un programa que nos pida por teclado dos calificaciones numéricas de un
alumno y nos muestre la media aritmética resultante redondeada sin decimales. Las
notas introducidas deben de estar entre 0 y 10 y admiten decimales. Caso de que una
entrada sea errónea debería de advertirnos de ello y no hacer el cálculo
"""
primeraNota=float(input("Introduce la nota del alumno: "))
segundaNota=float(input("Introduce la nota del alumno: "))
if 0 <=primeraNota <= 10 and 0 <=segundaNota <= 10:
    mediaAritmeica=(primeraNota+segundaNota)/2
    print(round(mediaAritmeica,2))
else:
    print("Error: Las notas deben estar entre 0 y 10. No se ha realizado el cálculo.")