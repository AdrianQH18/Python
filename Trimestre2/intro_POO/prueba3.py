"""profesores =["Agustin","Natalia","Javier"]
iterador= iter(profesores)
print(next(iterador))
print(next(iterador))
print(next(iterador,"No hay mas profes"))"""

class DiasdelaSemana:
    def __init__(self,dia):
        self.dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        self.indice=dia

    @property
    def indice(self):
        return

    @indice.setter
    def indice(self,value):
        pass

    def mostar(self):
        print(self.dias[self.indice])

    def __iter__(self):
        return self

    def __next__(self):
        dia_actual=self.dias[self.indice]
        if self.indice==len(self.dias)-1:
            self.indice=0
        else:
            self.indice+=1
        return dia_actual
dia = DiasdelaSemana(2)
dia.mostar()

iterador=iter(dia)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
