import re
try:
    fichero=open("telefonos.txt","rt")
    linea=fichero.readline()
    regexTelefonoMovil=r'^[6-8]\d{8}$'
    regexTelefono=r'^[6-8]\d{8}$|^00[0-9]{11}'
    regexNumSegundos=r'^[0-9]{2}'

    while linea != "":
        if re.match(regexTelefonoMovil,linea):
        print(linea)
        linea = fichero.readline()
    linea = fichero.close

except:
    print("Error, no se puede leer")