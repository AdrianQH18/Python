lista=[34,"PEPE",False,255,556,27,38,[1,2,3]]
print(lista)
lista4=["PEPE","PAPA","PIPI"]
lista.append("Nuevo Elemento")
print(lista)
lista2= lista+[23,45]
print(lista2)
lista3=lista2+lista
print(lista3)
lista.insert(2,15)
print(lista)
print(lista.count(34))

texto=str(lista4)
print(texto)
texto=texto.replace("[","")
texto=texto.replace("]","")
print(texto)

texto2="Hola Mundo"
lista5=list(texto2)
print(lista5)
matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz[1][0])
print(lista3)
print(lista3[:5])

