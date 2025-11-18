import random
#La palabra clave no se puede repetir
#Si lo hace el valor de la segunda clave sobreescribe al anterior valor asociado a dicha clave
dic1={}
dic2=dict()
dic3={"Nombre":"Sara","Edad":57,"Solterx":True}
dic4=dict(Primero='Uno',Tercero='Tres')
dic4["Segundo"]="Dos"

dic3.update(dic4)
print(dic3)
print(dic2)
#for que recorre el diccionario mostrando las claves
for elemento in dic3:
    print(elemento)
print()

#for que recorre el diccionario mostrando solo los elementos
for elemento in dic3:
    print(dic3[elemento])
print()

#for que recorre el diccionario mostrando clave y su valor "clave : valor"
for elemento in dic3:
    print(elemento,":",dic3[elemento])
print()

#for que recorre el diccionario mostrando clave y su valor "clave : valor" almacenandolos en las variables clav,valor
for clave,valor in dic3.items():
    print(clave,":",valor)

print()

print(dic3["Edad"])

#Muestra el valor de la clave edad con el metodo get
print(dic3.get("Edad"))
#se le asigna nuevo valor a la clave Edad
dic3["Edad"]=44
#si la clave no existe dentro del diccionario lo que hara sera crearla y asignarle el valor indicado en este caso Base de datos
dic3["Asignatura"]="Bases de datos"
print(dic3)

#si la clave no existe mostraria none pero lo podemos cambiar
print(dic3.get("Titulo","No encontrado"))
"""
print()
#El pop borra la pareja clave valor de la clave que le pasemos
print(dic3.pop("Edad"))
print(dic3)

print()
#El popitem borra el ultimo clave valor que le hayamos insertado al diccionario
print(dic3.popitem())
print(dic3)
"""
print()
print()
#dentro del diccionario podemos meterle valores como listas etc
d1=dict(Sara=[1,2,3],Pepe=55,Luis=44,Manolo=33,Eva=66,Ines=55)
print(d1)
def eliminaAlAzar(d1):
    elemento=random.sample(list(d1.keys()),1)
    d1.pop(elemento[0])
    print(d1)
eliminaAlAzar(d1)