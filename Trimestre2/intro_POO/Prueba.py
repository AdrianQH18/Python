class Perro:
    numPerros=0
    def __init__(self,nombre="ARIANA"):

        self.nombre=nombre
        Perro.numPerros+=1
        #self._secreto=secreto
        #self.__secretisimo=secretisimo

    def llamar(self):
        return "Ey "+self.nombre+" Ven Aqui!"

    @classmethod
    def cuantosPerros(cls):
        return cls.numPerros

    @staticmethod
    def ladrar():
        return "Dice: Guau"

    def sobrecargada(self,atributo):
        if isinstance(atributo, int):
            print("Trabajo con un numero")
        if isinstance(atributo, float):
            print("Trabajo con un numero")
        elif isinstance(atributo, str):
            print("Trabajo con un numero")
        elif isinstance(atributo, list):
            print("Trabajo con un numero")

    def sobrecargada2(self,*atributos):
        if(len(atributos)==1):
            print("Recibo un parametro")
        elif(len(atributos)==2):
            print("Recibo dos parametro")
        elif (len(atributos) == 3):
            print("Recibo dos parametro")

mascota1=Perro("Andrea")
mascota2=Perro()
mascota3=Perro("Camila")

mascota3.sobrecargada(3)
mascota3.sobrecargada(3.5)
mascota3.sobrecargada("String")
mascota3.sobrecargada([1,2,3])

mascota2.sobrecargada2(1,2)
mascota2.sobrecargada2(1)
mascota2.sobrecargada2(1,"Hola",3.5,[1,2])
#print(mascota3.cuantosPerros())
#print(Perro.ladrar())
#print(mascota2.ladrar())

#print(mascota2.cuantosPerros())
#print(mascota1.cuantosPerros())
#print(mascota3.cuantosPerros())
#Perro.numPerros=10

"""
mascota2=Perro("Cuchi Cuchi","Cariñito mio","ANDREA")
print(mascota2.llamar())
mascota2._secreto="Engendro del Demonio"
print(mascota2._secreto)

#Aqui no esta usando el atributo privado de la clase si no nos esta creando un nuevo atributo
mascota2.__secretisimo="Elemento inmundo"

mascota2._Perro__secretisimo="Rata azmilclera"
print(mascota2._Perro__secretisimo)
print(mascota2.__secretisimo)
"""
#mascota1=Perro()
#print(mascota1.llamar())
#mascota2=Perro("CAMILA")
#print(mascota2.llamar())
#mascota1.nombre="YAMILE"
#print(mascota1.llamar())