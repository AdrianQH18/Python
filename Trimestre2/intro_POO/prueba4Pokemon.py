class Pokemon:
    def __init__(self,nombre):
        self.__nombre= nombre
        self.__evolucion= None

    def setEvolucion(self,pokemon):
            self.__evolucion=pokemon

    def mostrar(self):
        print(self.__nombre)

    def evoluciona(self):
        if self.__evolucion==None:
            print("Este pokemon no sabe evolucionar")
            evo=self
        else:
            print("Este pokemon a evolucionado")
            evo=self.__evolucion
        return evo
p1=Pokemon("Bulbasaur")
p2=Pokemon("Venasaur")
p1.mostrar()
p2.mostrar()
print()

p1.setEvolucion(p2)
p2=p2.evoluciona()
p1=p1.evoluciona()
print()

p1.mostrar()
p2.mostrar()