#Escribir un programa que pida por teclado un número al usuario y diga si es par o impar

numero=int(input("Introduce un numero para saber si es par o impar: "))

if numero%2==0:
    print("El numero ",numero," es par")
else:
    print("El numero ",numero," no es par")