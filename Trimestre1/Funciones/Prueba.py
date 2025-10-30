#def miFuncion():
#   otroTexto="Hola mundo Cruel"
#    texto="hola otra vez mundo"
#    print("Desde dentro de la funcion",texto)
#    return otroTexto

#texto="Hola Mundo"
#print("Valor devuelto",miFuncion())
#print("Desde fuera de la funcion",texto)

def miFuncion(parametro, parametro2):
    for i in range(parametro2):
        print(parametro)

texto="Hola Mundo"
miFuncion(texto,3)
miFuncion("hola mundo cruel",2)