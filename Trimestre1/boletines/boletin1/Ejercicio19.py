"""
Escribir un programa que pida un número por teclado y nos muestre sus divisores
"""
num=int(input("Introduce un numero: "))
for i in range(1,num+1):
    if num%i==0:
        print(i)