"""
Escribir un programa que nos pida tres números por teclado en cualquier orden y nos los
muestre en pantalla ordenados de menor a mayor
"""
num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))
num3=int(input("Introduce el tercer numero: "))
menor=min(num1,num2)
mayor=max(num1,num2)
if num3<menor:
    print(num3," ",menor," ",mayor)
elif num3>menor and num3<mayor:
    print(menor, " ",num3," ", mayor)
else:
    print(menor, " ", mayor," ",num3)
"""
lista=[num1,num2,num3]
lista.sort()
print(lista)
"""
