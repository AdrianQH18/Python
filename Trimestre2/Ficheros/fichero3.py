import pickle
class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def ver(self):
        print(self.nombre+"("+str(self.edad)+")")

p1=Persona("pepe",1)
p2=Persona("Ana",66)
lista=[p1,p2]

try:
    fichero=open("personas.bin","wb")
    pickle.dump(lista,fichero)
    pickle.dump(p2, fichero)
    fichero.close()


    fichero=open("personas.bin","rb")
    lista=pickle.load(fichero)
    for elemento in lista:
        print(type(elemento))
        elemento.ver()

    fichero.close()

except:
    print("Error, no se puede hacer")