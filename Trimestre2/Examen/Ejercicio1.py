from abc import ABC, abstractmethod

class Conductor:
    def __init__(self, nombre,nif,anoNacimiento,anoCarnet,puntosCarnet):
        self.nombre = nombre
        self.nif = nif
        self.anoNacimiento = anoNacimiento
        self.anoCarnet = anoCarnet
        self.puntosCarnet = puntosCarnet

    def calcularEdad(self):
        edad=2025-self.anoNacimiento
        return edad
    def calcularTiempoCarnet(self):
        antiguedadCarnet=2025-self.anoCarnet
        return antiguedadCarnet
    def __str__(self):
        return f"Conductor: {self.nombre}. Edad: {self.calcularEdad()}. Años de carnet: {self.calcularTiempoCarnet()}. Puntos: {self.puntosCarnet}"


class Vehiculos(ABC):
    def __init__(self,matricula,annoVenta,conductor):
        self.matricula = matricula
        self.annoVenta = annoVenta
        self.conductor = conductor

class Moto(Vehiculos):
    def __init__(self,matricula,annoVenta,conductor):
        super().__init__(matricula,annoVenta,conductor)

    def calcularSeguroTodoRiesgo(self):
        return "No hay seguro a todo riesgo para motos"

    def calcularAntiguedad(self):
        antiguedad=2025-self.annoVenta
        return antiguedad

    def calcularSeguroTerceros(self):
        seguroTerceros=250
        if self.calcularAntiguedad()<8:
            seguroTerceros+=100
        if self.conductor.calcularEdad()<24:
            seguroTerceros+=250+50
        if self.conductor.calcularTiempoCarnet()<2:
            seguroTerceros+=250+75
        return seguroTerceros

    def __str__(self):
        return f"Vehiculo:Moto Matricula: {self.matricula}. Año de compra: {self.annoVenta}"

class Coche(Vehiculos):
    def __init__(self, matricula, annoVenta,conductor):
        super().__init__(matricula, annoVenta,conductor)

    def calcularAntiguedad(self):
        antiguedad=2025-self.annoVenta
        return antiguedad

    def calcularSeguroTodoRiesgo(self):

        if self.calcularAntiguedad()==0:
            seguroTodoRiesgo=400
        elif self.calcularAntiguedad()==1:
            seguroTodoRiesgo=500
        elif self.calcularAntiguedad()==2:
            seguroTodoRiesgo=700
        elif self.calcularAntiguedad()>=3:
            seguroTodoRiesgo=250
        elif self.conductor.puntosCarnet<8:
            seguroTodoRiesgo=400+100
        return f"Precio del seguro a todo riesgo: {seguroTodoRiesgo}"

    def calcularSeguroTerceros(self):
        seguroTerceros=250
        if self.conductor.puntosCarnet<8:
            seguroTerceros+=100
        if self.conductor.calcularEdad()<24:
            seguroTerceros+=50
        if self.conductor.calcularTiempoCarnet()<2:
            seguroTerceros+=75
        return f"Precio del seguro a terceros: {seguroTerceros}"

    def __str__(self):
        return f"Vehiculo:Coche Matricula: {self.matricula}. Año de compra: {self.annoVenta}"




conductor1=Conductor("Jose Maria","1312313C",2004,2020,10)
coche1=Coche("6310NXB",2024,conductor1)

conductor2=Conductor("Adrian Quispe","1312313C",1990,2024,8)
moto1=Moto("1312NXB",2000,conductor2)

print(coche1)
print(conductor1)
print(coche1.calcularSeguroTodoRiesgo())
print(coche1.calcularSeguroTerceros())
print()
print(moto1)
print(conductor2)
print(moto1.calcularSeguroTodoRiesgo())
print(moto1.calcularSeguroTerceros())