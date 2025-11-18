#def miFuncion():
#   otroTexto="Hola mundo Cruel"
#    texto="hola otra vez mundo"
#    print("Desde dentro de la funcion",texto)
#    return otroTexto

#texto="Hola Mundo"
#print("Valor devuelto",miFuncion())
#print("Desde fuera de la funcion",texto)
"""
def miFuncion(parametro, parametro2):
    for i in range(parametro2):
        print(parametro)

texto="Hola Mundo"
miFuncion(texto,3)
miFuncion("hola mundo cruel",2)"""


"""
def saludo(nombre,mensaje="hola",despedida="Hasta la vista"):
    print(mensaje,nombre,despedida)

saludo("José Maria",despedida="Nos vemos pronto")
saludo("José Maria", "Bienvenida",)


def argumentosVariables(nombre, *titulos):
    for titulo in titulos:
        print(titulo, end=" ")
    print(nombre)
argumentosVariables("José Maria","Sr")
argumentosVariables("José Maria","EXcelentisimo","Ilustrisimo","Sr","Don")"""




"""
lista=["ANA","Pedro","Luis"]
for nombre in lista:
    print(nombre)

print()
for i in range(len(lista)):
    print(i,"-",lista[i])
print()
for i, nombre in enumerate(lista):
    print(i,"-",nombre)
"""



numero1=[7]
numero2=numero1.copy()
numero2[0]=numero2[0]*2
print(numero2)
print(numero1)

