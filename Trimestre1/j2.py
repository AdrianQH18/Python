"""
#if-else
edad=int(input("dame tu edad: "))
if edad>=18:
    print("Eres mayor de edad")
#si el poblque esta vacio puedes usar pass para que no te de error
elif edad<=18:
    print("Eres menor de edad")
else:
    pass
print("Pograma finalizado")
#Condiciones que se pueden usar en los if son and y or, como <,> o ==

#booleanos
acertado=False
if not acertado:
    print("opcion1")
else:
    print("opcion2 ")

for n in range(20,0,-2):
    print(n,end=",")
print("\b")

for m in "hola mundo":
    if(m!=" "):
        print(m, end=",")
print("\b")


edad= int(input("Introduce tu edad: "))

print("te faltan ", 67-edad," años para jubilarte")

"""
"""
texto="hola Mundo"
print(len(texto))

print(texto[3:8])
print(texto[:8])
print(texto[3:])
print(texto[-2])
print(texto.upper())
print(texto.lower())
print(texto.swapcase())

print(texto.find("a"))

print(texto.count("o"))

print(texto.replace("o","a",9))
"""


tuplas=(1,2,3,4,5)
print(tuplas)
lista=list(tuplas)
lista.append(6)
texto=str(tuplas)
print(texto)

tupla1="pepe","juan","Ana"
print(tupla1)