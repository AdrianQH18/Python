#2. Tenemos un fichero llamado estadisticas.txt. El formato del fichero es el siguiente (pero el
#contenido puede variar, lógicamente):
#Hombre
#1.73
#Mujer
#1.68
#Mujer
#1.83
#Realiza un programa que lea el contenido de ese fichero y muestre el número de hombres, el
#número de mujeres y la altura media (con dos decimales) de todos sin hacer distinción de sexo.
#Por ejemplo, para el fichero del ejemplo anterior, la salida del programa sería esta:
#Hombres: 1.
#Mujeres: 2.
#Estatura media: 1.75
#El formato del fichero se supone correcto y comprobado y nunca va dar problemas

def contado(estadisticas):
    contadorHombres=0
    contadorMujeres=0

    try:
        with open(estadisticas, 'r') as ficheroA:
            linea = ficheroA.readlines()
            for linea in linea:
                linea = linea.strip()
                if linea =="Hombre":
                    contadorHombres+=1
                elif linea =="Mujer":
                    contadorMujeres+=1
    except:
        print("No hay estadisticas")

    print("Hombre:",contadorHombres)
    print("Mujer:",contadorMujeres)

def alturaMedia(estadistica):
    sumaAlturas=0
    cantidad=0
    try:
        with open(estadistica, 'r') as ficheroA:
            lineas = ficheroA.readlines()
            for i in range(1,len(lineas),2):
                altura_str = lineas[i].strip()
                altura=float(altura_str)
                sumaAlturas+=altura
                cantidad+=1
        mediaAltura=sumaAlturas/cantidad
        print(f"Estatura media: {mediaAltura:.2f}")
    except:
        print("No hay estadisticas")

def main():
    contado("estadisticas.txt")
    alturaMedia("estadisticas.txt")
main()