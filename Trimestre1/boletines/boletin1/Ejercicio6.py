#Escribir un programa que pida por teclado un número al usuario y diga si es divisible por 3 o no
numero= int(input("Introduce un numero para saber si es divisible entre 3: "))
if numero%3==0:
    print("El numero ",numero," es divisible entre 3")
else:
    print("El numero ", numero, "no es divisible entre 3")