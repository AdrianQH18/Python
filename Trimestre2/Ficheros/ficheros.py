try:
    fichero = open('quijote.txt','rt')  # Abre el fichero indicado
    #texto = fichero.read()
    lineas = fichero.readlines()

    for i in range(len(lineas)):
        if lineas[i][-1] == '\n':
            lineas[i]=lineas[i][:-1]

    print(lineas)
    fichero.close()
except:
    print("Error, el fichero no existe")
    #cierra el fichAero que se a abierto