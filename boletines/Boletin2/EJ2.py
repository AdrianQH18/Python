"""
Idem al anterior pero ordenando ahora en orden descendente
"""
palabra1=input("Introduce primera palabra: ")
palabra2=input("Introduce segundo palabra: ")
palabra3=input("Introduce tercera palabra: ")

ultimo=min(palabra1,palabra2)
primero=max(palabra1,palabra2)
if palabra3>primero:
    print(palabra3," ",primero," ", ultimo)
elif palabra3<ultimo:
    print(primero, " ", ultimo, " ", palabra3)
else:
    print(primero, " ", palabra3, " ", ultimo)