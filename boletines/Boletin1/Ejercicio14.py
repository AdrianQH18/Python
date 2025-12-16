#Escribir un programa que nos pida dos números por teclado y genere un número aleatorio
#comprendido entre ambos. Por el momento no te preocupes de que el primer número
#siempre debería de ser menor que el segundo, simplemente no los metas en un orden
#incorrecto
import random

num1=int(input("Introduzca el primer numero: "))
num2=int(input("Introduzca el segundo numero: "))

numAleatorio=random.randint(num1,num2)
print("Numero aleatorio es: ",numAleatorio)