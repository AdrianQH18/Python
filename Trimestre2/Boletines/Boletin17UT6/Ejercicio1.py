"""1. Crea una función en python que se llame compararFicheros y que reciba como argumento el
nombre de dos ficheros de texto. La función debería de devolver un valor booleano indicando
si el contenido de ambos ficheros es exactamente el mismo o no"""

def compararFichero(fichero1,fichero2):
    try:
        with open(fichero1, 'r') as ficheroA:
            with open(fichero2, 'r') as ficheroB:
                iguales= ficheroA.read()==ficheroB.read()
                return iguales

    except:
        print("Error, no se puede cargar")

def main():
    print("Los ficheros son iguales:")
    print(compararFichero('fichero1.txt','fichero2.txt'))
main()