"""
Escribir un programa que pida por teclado un número al usuario y calcule si es primo o no
"""
num=int(input("Introduce un numero primo: "))
contador=0
for i in range(1,num+1):
    if num%i==0:
        contador+=1
if contador==2:
    print("El numero es primo")
else:
    print("El numero no es primo")