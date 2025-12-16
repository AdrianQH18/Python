class Ciclo:
    def __init__(self,nombre,grado):
        self.nombre=nombre
        self.grado=grado
        self.modulos=[]

    def anadir(self,modulo):
        self.modulos.append(modulo)