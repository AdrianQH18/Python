texto=input("Escribe el texto: ")
vocales=["a","e","i","o","u","A","E","I","O","U"]
contEspacios=0
cadenaFinal=""
contVocales=0
for i in texto:
    if i==" ":
        contEspacios+=1
    elif i in vocales:
        contVocales+=1
    else:
        cadenaFinal=cadenaFinal+i
print("sin vocales ni espacios: ",cadenaFinal)
print("Vocales suprimidas: ",contVocales)
print("Espacios en blancos suprimidos: ",contEspacios)