#Escribir un programa que nos pida por teclado dos calificaciones numéricas de un
#alumno y nos muestre la media aritmética resultante redondeada sin decimales. Las
#notas introducidas deben de estar entre 0 y 10 y admiten decimales. Caso de que una
#entrada sea errónea debería de advertirnos de ello y no hacer el cálculo

nota1=int(input("introduce nota1:"))
nota2=int(input("introduce nota2:"))
if nota1>10 or nota1<0 or nota2>10 or nota2<0:
    print("nota invalida")
mediaAritmetica=(nota1+nota2)/2
print(mediaAritmetica)