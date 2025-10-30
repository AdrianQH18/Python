profesorPrimero={"Ana","Juan Carlos","Sancho","Natalia"}
print(profesorPrimero)
profesorSegundo=set(["Agustin","Ana","Natalia","Javier","Jose Maria"])
print(profesorSegundo)

if "Juan Carlos" in profesorPrimero:
    print("Juan Carlos da clase en Primero")
if "Javier" not in profesorPrimero:
    print("Javier no da clase en Primero")

for elemento in profesorPrimero:
    print(elemento)

print(len(profesorPrimero))

for i in range(0,len(profesorPrimero)):
    #print(profesorPrimero[i])
    print("Hola")
profesorPrimero.add("Jose Maria")
print(profesorPrimero)
profesorPrimero.add("Jose Maria")
print(profesorPrimero)
profesorPrimero.remove("Jose Maria")
print(profesorPrimero)
profesorPrimero.discard("Jose Maria")
print(profesorPrimero)

profe=profesorPrimero.pop()
print(profe)
print(profesorPrimero)

#profesorPrimero.clear()
#print(profesorPrimero)
print()
print()
print()
conjunto1=set([1,2,3,2,2,2,4,5,2,1,6])
print(conjunto1)

conjunto2=set("Hola mundo cruel")
print(conjunto2)
print()
print()
print()

lista=list(profesorPrimero)
print(lista)
tupla=tuple(profesorPrimero)
print(tupla)
texto=str(profesorPrimero)
print(texto)

print()
print()
print()

print(profesorPrimero | profesorSegundo)
print(profesorPrimero & profesorSegundo)
print(profesorPrimero - profesorSegundo)
print(profesorSegundo - profesorPrimero)
print(profesorPrimero ^ profesorSegundo)

#print(profesorPrimero.union(profesorSegundo))
#print(profesorPrimero.intersection(profesorSegundo))
#print(profesorPrimero.difference(profesorSegundo))
#print(profesorSegundo.difference(profesorPrimero))
#print(profesorPrimero.symmetric_difference(profesorSegundo))
