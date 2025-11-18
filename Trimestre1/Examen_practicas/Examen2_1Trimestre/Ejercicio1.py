def numeroPin(pin):
    pinManejable=str(pin)
    lista=[ "XXXXXXXXXX",
            "XXXXXXXXXX",
            "XXXXXXXXXX",
            "XXXXXXXXXX"]
    listaModificada=list(lista)
    for i in range(len(pinManejable)):
        posicion=int(pinManejable[i])
        elemento=listaModificada[i]
        if posicion==0:
            posicion=-1
        temp=list(elemento)
        temp[posicion]="O"
        listaModificada[i]="".join(temp)
    for j in listaModificada:
        print(j)

numeroPin(6240)