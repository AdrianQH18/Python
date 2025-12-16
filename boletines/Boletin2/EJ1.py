"""
Escribir un programa que nos pida tres palabras por teclado en cualquier orden y nos
las muestre en pantalla ordenadas alfabeticamente en orden ascendente
"""
palabra1=input("Introduce primera palabra: ")
palabra2=input("Introduce segundo palabra: ")
palabra3=input("Introduce tercera palabra: ")

primero=min(palabra1,palabra2)
ultimo=max(palabra1,palabra2)
if palabra3<primero:
    print(palabra3," ",primero," ", ultimo)
elif palabra3>ultimo:
    print(primero, " ", ultimo, " ", palabra3)
else:
    print(primero, " ", palabra3, " ", ultimo)