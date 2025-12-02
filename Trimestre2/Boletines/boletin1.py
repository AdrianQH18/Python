import random


class Pokemon:
    def __init__(self,codigo,nombre,tipo):
        self.__codigo=codigo
        self.__nombre= nombre
        self.__tipo= tipo
        self.__evolucion= None

        self.__pv=random.randint(50,100)

    def setEvolucion(self,pokemon):
            self.__evolucion=pokemon

    def mostrar(self):
        print(self.__nombre,"- PV:",self.__pv)

    def evoluciona(self):
        if self.__evolucion==None:
            print("Este pokemon no sabe evolucionar")
            evo=self
        else:
            evo=self.__evolucion
        return evo

    def combateContra(self,contricante):
        daño=random.randint(25,50)
        contricante.__pv -= daño
        if contricante.__pv!=0:
            daño =random.randint(25,50)
            self.__pv-=daño
            if self.__pv<=0:
                print(self.__nombre,"Ha sido derrotado")
            else:
                print("Ninguno de los pokemones ha sido vencido")
        else:
            print(contricante.__nombre,"ha sido derrotado")

p1=Pokemon(1,"Bulbasaur","Planta")
p2=Pokemon(2,"Venasaur","Planta")
p1.mostrar()
p2.mostrar()
print()

p1.setEvolucion(p2)
p1.mostrar()
print()

p1=p1.evoluciona()
p2=p2.evoluciona()
p1.mostrar()
p2.mostrar()

p3=Pokemon(3,"Pikachu","Electrico")
p3.combateContra(p1)