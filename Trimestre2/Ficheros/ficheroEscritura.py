try:
    with open("quijote.txt","at")as fichero:
        fichero.write("UNO\n")
        fichero.write("DOS\n")
        fichero.write("TRES\n")


    """lista=["Jorge","Eva","Ana","Pepa"]
    fichero.writelines(lista)
    fichero.close()"""
except:
    print("Error, el fichero no existe")