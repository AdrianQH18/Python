import random
lista=[]
contador=0
salir=False
while not salir:
    numero = int(input("Escribe un numero: "))
    if numero>=10:
        print("5 numeros pares aleatorios y diferentes comprendidos entre el 1 y el ", numero, ":")
        while contador<5:
            numeroRandom=random.randint(1,numero)
            if numeroRandom%2==0:
                if numeroRandom not in lista:
                    lista.append(numeroRandom)
                    contador+=1
                    print(numeroRandom)
        salir=True
    else:
        print("Error...numero debe ser mayor que 10: ")
